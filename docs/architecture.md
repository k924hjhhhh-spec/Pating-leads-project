# Painting Leads — Production Architecture

## Purpose
South Florida painting-lead marketplace for Broward and Palm Beach first.

## Runtime layers
1. Public intake receives homeowner requests.
2. Workflow: ALEX 1 → MAX 2 → RYAN 3 → LUCAS 4 → JACK 5 → LEO 6 → ETHAN 7 → SAM 8.
3. Shared state stores one canonical lead/job record.
4. Human controls provide review, override, pause, and audit history.
5. GitHub main is the source of truth; Cloudflare publishes the deployed application.

## Environments
- Local: developer testing only; secrets come from environment variables.
- Staging: test leads, test contractors, and test notifications.
- Production: real operations; no test data.

## Initial lifecycle
NEW → INTAKE_COMPLETE → QUALIFIED → ESTIMATED → MATCHED → OFFERED → ACCEPTED → SCHEDULED → COMPLETED → PAID → REVIEWED

Terminal states: REJECTED, EXPIRED, CANCELLED, DISPUTED.

## Security boundaries
- Never commit API keys, Cloudflare tokens, customer credentials, or payment secrets.
- Store secrets only in runtime/platform secret storage.
- Separate customer data from public dashboard presentation.
- Require human approval before real outbound messages or payments during pilot.

## Current baseline
- FastAPI service with /health and /intake.
- ALEX 1 is implemented; later agents need data contracts, approval gates, and audit logging.
- Dashboard is a control-center prototype, not yet verified as a live operations system.

## Task 2 acceptance criteria
Architecture, environments, lifecycle, deployment path, and security boundaries are documented so future implementation uses one shared lifecycle and does not mix staging with production.
