# Staging and Production Configuration

## Staging
Purpose: safe development and test leads.
- Separate deployment/service from production.
- Use test data only.
- Use mock notifications and payment providers.
- Use non-production API credentials.
- Enable verbose diagnostics without exposing secrets.
- Require manual promotion to production.

## Production
Purpose: approved real operations.
- Use platform-managed secrets only.
- Disable debug output and test-mode shortcuts.
- Apply least-privilege credentials.
- Protect customer data and uploaded media.
- Require approval gates for outbound messages and payments during pilot.

## Shared configuration
- Environment name
- Application version
- OpenAI model settings
- Service-area settings
- Feature flags
- Logging level
- Notification mode
- Payment mode

No secret belongs in GitHub, HTML, screenshots, or chat.
