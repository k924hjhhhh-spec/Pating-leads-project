# Project Readiness Checklist

## Repository
- [x] GitHub repository exists and main branch is accessible.
- [x] README describes the current runnable slice.
- [x] Architecture and lifecycle are documented.
- [ ] Automated tests cover all active endpoints.
- [ ] CI status is configured and passing.

## Application
- [x] /health endpoint exists.
- [x] /intake endpoint exists.
- [ ] Lead persistence exists.
- [ ] MAX 2 qualification is implemented.
- [ ] Human review queue exists.
- [ ] Public dashboard uses live, privacy-safe data.

## Operations
- [ ] Staging deployment is separated from production.
- [ ] Secrets are stored only in runtime secret storage.
- [ ] Rollback procedure is tested.
- [ ] Real outbound messages remain disabled until approved.
- [ ] Payment actions remain disabled until approved.

## Launch gate
MVP is not production-ready until every unchecked launch-critical item has an owner, test evidence, or an explicit user decision.
