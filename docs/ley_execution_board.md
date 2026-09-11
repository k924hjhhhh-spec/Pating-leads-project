# LEY — Painting Leads Execution Board

Updated: 2026-09-11
Scope: Broward + Palm Beach
Real operation: **NOT RELEASED**

## Verified progress

1. **ALEX → MAX → RYAN → LUCAS → JACK → LEO → ETHAN → SAM** — full Supabase staging RPC executed successfully with fictional data inside a transaction and rolled back. Final simulated status: `closed`; messages sent: 0; money moved: false; ads published: 0.
2. **Staging database** — `painting-leads-staging` remains isolated, ACTIVE_HEALTHY, with 11 RLS-protected tables. Post-test counts verified at 0 leads, 0 contractors, 0 events, 0 distributions, 0 appointments, 0 fee events and 0 SAM records.
3. **Remote staging intake security** — `painting-leads-intake` upgraded to v2 with JWT verification enabled, explicit CORS preflight handling, strict allowed origin, JSON-only input, 16 KB body enforcement based on actual bytes, required UUID idempotency key, no-store responses and safer error handling.
4. **RPC defects fixed** — corrected over-escaped phone/email regexes that prevented the remote fictional E2E from running and removed score variable ambiguity.
5. **JACK lifecycle defect fixed in GitHub** — expired offers can no longer be accepted.
6. **Duplicate detection fixed in GitHub** — US `+1` phone format now normalizes consistently with 10-digit domestic format.
7. **Regression coverage added** — tests added for expired-offer rejection and +1 duplicate normalization.
8. **Source control alignment started** — hardened Edge Function source and the Supabase migration are now tracked in the canonical repository.
9. **Security advisor** — Supabase security advisor returned no current lints after the migration.

## Next unlocked execution

- Sync the verified 09/10 `website/` TESTE implementation into the canonical repository; GitHub main is currently missing that local website slice even though it exists in the authoritative checkpoint/patch.
- Add a private staging adapter for the homeowner form to call the JWT-protected Edge Function with a publishable client key and UUID idempotency key; keep local TESTE mode available.
- Run source-level contract tests for the private staging adapter and confirm browser preflight/auth behavior when a reachable private preview is available.
- Preserve separate contact consent and partner-sharing consent before any real distribution path.
- Add secure remote photo-storage design before enabling photos outside local TESTE mode.
- Add partner onboarding/coverage fixtures for Broward first, Palm Beach separately, without contacting real contractors.
- Expand LEO → ETHAN → SAM negative-path tests: no-show, cancellation, complaint, refund/fee reversal placeholders, all with no money movement.

## Owner-blocked / real-world gates

- Real contractor onboarding and coverage verification.
- Final pricing / commission model and commercial terms.
- Final privacy / consent / legal wording.
- Public publication, paid acquisition, customer contact, contractor contact and any money movement.

## Execution rule

Ley advances every safe, reversible internal task, tests it, records evidence and skips owner-blocked work. No fabricated live metrics, no cross-project data, no customer/contractor contact, no payments and no public launch without the required approval.
