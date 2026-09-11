import { createClient } from 'jsr:@supabase/supabase-js@2';

const ALLOWED_ORIGIN = 'https://painting-leads-staging.netlify.app';
const MAX_BODY_BYTES = 16 * 1024;
const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

function corsHeaders(origin: string) {
  return {
    'access-control-allow-origin': origin,
    'access-control-allow-methods': 'POST, OPTIONS',
    'access-control-allow-headers': 'authorization, apikey, content-type, idempotency-key',
    'access-control-max-age': '600',
    'vary': 'Origin',
  };
}

function jsonResponse(body: unknown, status: number, origin = '') {
  const headers: Record<string, string> = {
    'content-type': 'application/json; charset=utf-8',
    'cache-control': 'no-store',
    'x-content-type-options': 'nosniff',
  };
  if (origin === ALLOWED_ORIGIN) Object.assign(headers, corsHeaders(origin));
  return new Response(JSON.stringify(body), { status, headers });
}

Deno.serve(async (req: Request) => {
  const origin = req.headers.get('origin') ?? '';

  if (origin !== ALLOWED_ORIGIN) {
    return jsonResponse({ error: 'Origin not allowed' }, 403);
  }

  if (req.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders(origin) });
  }

  if (req.method !== 'POST') {
    return jsonResponse({ error: 'Method not allowed' }, 405, origin);
  }

  const contentType = req.headers.get('content-type') ?? '';
  if (!contentType.toLowerCase().startsWith('application/json')) {
    return jsonResponse({ error: 'JSON required' }, 415, origin);
  }

  const idempotencyKey = (req.headers.get('idempotency-key') ?? '').trim();
  if (!UUID_RE.test(idempotencyKey)) {
    return jsonResponse({ error: 'Valid idempotency-key required' }, 400, origin);
  }

  try {
    const rawBody = await req.text();
    const bodyBytes = new TextEncoder().encode(rawBody).byteLength;
    if (bodyBytes <= 0 || bodyBytes > MAX_BODY_BYTES) {
      return jsonResponse({ error: 'Body limit' }, 413, origin);
    }

    let payload: Record<string, unknown>;
    try {
      const parsed = JSON.parse(rawBody);
      if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
        return jsonResponse({ error: 'Object required' }, 422, origin);
      }
      payload = parsed as Record<string, unknown>;
    } catch {
      return jsonResponse({ error: 'Invalid JSON' }, 400, origin);
    }

    payload.origin = origin;
    payload.idempotency_key = idempotencyKey;

    const supabaseUrl = Deno.env.get('SUPABASE_URL');
    const serviceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY');
    if (!supabaseUrl || !serviceRoleKey) {
      return jsonResponse({ error: 'Staging operation unavailable' }, 503, origin);
    }

    const supabase = createClient(supabaseUrl, serviceRoleKey, {
      auth: { persistSession: false, autoRefreshToken: false },
    });
    const { data, error } = await supabase.rpc('painting_leads_staging_e2e', { payload });
    if (error) {
      console.error('painting_leads_staging_e2e failed', error.code ?? 'unknown');
      return jsonResponse({ error: 'Staging operation unavailable' }, 422, origin);
    }

    return jsonResponse(data, 201, origin);
  } catch (error) {
    console.error('painting-leads-intake unexpected failure', error instanceof Error ? error.name : 'unknown');
    return jsonResponse({ error: 'Staging operation unavailable' }, 503, origin);
  }
});
