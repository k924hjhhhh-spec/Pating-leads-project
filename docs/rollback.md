# Rollback and Recovery

1. Identify the last known-good GitHub commit.
2. Confirm the failing deployment and affected surface.
3. Pause real outbound notifications and payment actions.
4. Revert through a reviewed GitHub change or redeploy the known-good commit.
5. Verify the deployment build completes.
6. Verify the public landing page and /health endpoint.
7. Run the smoke-test checklist.
8. Record the incident, cause, change, and recovery result.
9. Reopen paused workflows only after human approval.

Never delete production data during recovery. Preserve logs and audit events.
