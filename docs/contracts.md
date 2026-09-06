# Worker Contracts

Every worker receives a validated record and returns a structured internal result.

## Common result
- lead_id
- worker
- input_state
- output_state
- decision
- confidence
- missing_fields
- risk_flags
- evidence
- created_at
- audit_event

## Worker handoffs
- ALEX 1: raw request → INTAKE_COMPLETE
- MAX 2: intake → QUALIFIED or REJECTED
- RYAN 3: qualified intake → ESTIMATED
- LUCAS 4: job card → MATCHED
- JACK 5: matches → OFFERED draft
- LEO 6: accepted offer → SCHEDULED draft
- ETHAN 7: completed job → PAID record
- SAM 8: paid/completed record → REVIEWED

## Validation
- Reject missing lead_id.
- Reject invalid state transitions.
- Preserve raw input for audit, but redact it from public views.
- Do not pass private customer contact details to workers that do not need them.
- Do not mark an external action complete until a provider confirms it.
