# Security Rules

- Never commit API keys, Cloudflare tokens, payment secrets, customer credentials, or private contact data.
- Read secrets only from runtime environment variables or platform secret storage.
- Do not place secrets in HTML, logs, GitHub issues, screenshots, or chat messages.
- Keep staging data separate from production data.
- Redact phone, email, address, and uploaded media from public dashboard views.
- Require explicit approval before real outbound messages, contractor offers, or charges during pilot.
- Record audit events for authentication, state changes, overrides, exports, and payment actions.
- Rotate any credential that appears in a screenshot or message.
