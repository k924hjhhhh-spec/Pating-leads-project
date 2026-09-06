# Shared Data Model

## Lead
- id
- created_at
- source
- homeowner_contact
- property
- project_scope
- qualification
- estimate
- job_card
- matching
- distribution
- scheduling
- payment
- outcome
- lifecycle_state
- audit_events

## Required intake fields
- name
- phone or email
- city/ZIP
- interior or exterior
- service type
- approximate size or rooms
- condition
- timeline
- photo/video availability
- consent

## Data principles
- Use one canonical lead ID across all eight workers.
- Keep raw customer input separate from normalized fields.
- Treat estimates as preliminary until human/contractor confirmation.
- Never expose private contact data in public dashboard counters.
- Validate every worker output before passing it forward.
