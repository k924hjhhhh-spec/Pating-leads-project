# LEY Command Center — Worker Assignments

LEY owns sequencing and quality gates. Workers produce internal drafts until approval gates are opened.

| Worker | Owner of | Current assignment |
|---|---|---|
| ALEX 1 | Customer Intake | Normalize homeowner request into Lead |
| MAX 2 | Qualification & Scoring | Score service-area fit, completeness, value, urgency, contactability |
| RYAN 3 | Estimation & Job Card | Produce preliminary estimate and structured job card |
| LUCAS 4 | Contractor Matching | Rank eligible contractors without contacting them |
| JACK 5 | Job Distribution | Prepare offer drafts and response tracking |
| LEO 6 | Scheduling | Prepare appointment options and reminders |
| ETHAN 7 | Fees and Payments | Maintain fee ledger and payment plan; no charges |
| SAM 8 | Learning and Reviews | Record outcomes, reviews, and optimization signals |

## Execution rules
- One canonical lead ID travels through every worker.
- Each worker returns evidence, missing fields, risk flags, and next state.
- LEY blocks external messages, payments, and legal commitments without approval.
- Blocked work is skipped and logged with the exact missing dependency.
