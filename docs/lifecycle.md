# Lead Lifecycle

## States
- NEW: request received, not yet normalized.
- INTAKE_COMPLETE: ALEX 1 captured required intake fields.
- QUALIFIED: MAX 2 accepted the lead for the service area and minimum value.
- ESTIMATED: RYAN 3 created a preliminary estimate and job card.
- MATCHED: LUCAS 4 selected eligible contractors.
- OFFERED: JACK 5 sent an offer to approved contractors.
- ACCEPTED: contractor accepted the opportunity.
- SCHEDULED: LEO 6 confirmed an appointment window.
- COMPLETED: work/appointment outcome recorded.
- PAID: ETHAN 7 recorded the applicable fee/payment status.
- REVIEWED: SAM 8 recorded outcome, review, and learning data.

## Terminal states
REJECTED, EXPIRED, CANCELLED, DISPUTED.

## Rules
- Every transition records timestamp, actor, previous state, new state, and reason.
- A lead may not skip required stages.
- External messages and payment actions require an approval gate during pilot.
- Terminal states may only be reopened by an admin override with an audit reason.
