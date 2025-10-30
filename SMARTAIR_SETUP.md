# Smart Air Domain Monitoring Setup

## Automated Weekly Email Notifications

This repository is configured to automatically check domain expiration dates weekly and send email reports.

### GitHub Actions Workflow

The workflow runs weekly every Monday at 1:00 AM UTC (9:00 AM Singapore Time) and checks all domains in `smartair.txt`.

### Required GitHub Secrets

To enable email notifications via AWS SES, configure these secrets in your GitHub repository:

1. Go to: https://github.com/SmartAirTech/dns-domain-expiration-checker/settings/secrets/actions
2. Click "New repository secret" and add each of the following:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `AWS_SES_SMTP_ENDPOINT` | AWS SES SMTP endpoint for your region | `email-smtp.us-east-1.amazonaws.com` |
| `AWS_SES_SMTP_USERNAME` | SMTP credentials username from AWS SES | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SES_SMTP_PASSWORD` | SMTP credentials password from AWS SES | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `EMAIL_FROM` | Verified sender email address in SES | `alerts@smartair.com` |
| `EMAIL_TO` | Recipient email address(es) | `admin@smartair.com` |

### AWS SES Setup

1. **Create AWS Account** (if you don't have one)
   - Sign up at: https://aws.amazon.com/

2. **Verify Your Email Domain or Address**
   - Go to AWS SES Console: https://console.aws.amazon.com/ses/
   - Choose your region (e.g., `us-east-1`)
   - Click "Verified identities" → "Create identity"
   - Verify either:
     - **Domain**: `smartair.com` (recommended for production)
     - **Email address**: `alerts@smartair.com` (easier for testing)
   - Follow verification instructions (check DNS records or email)

3. **Create SMTP Credentials**
   - In SES Console, go to "SMTP settings"
   - Click "Create SMTP credentials"
   - Save the SMTP username and password (you can't retrieve password later!)
   - Note your SMTP endpoint (e.g., `email-smtp.us-east-1.amazonaws.com`)

4. **Request Production Access** (if needed)
   - New AWS SES accounts start in "sandbox mode"
   - Sandbox mode: can only send to verified addresses
   - Production mode: can send to anyone
   - Request production access in SES Console if needed

5. **Add Secrets to GitHub**
   - Use the SMTP credentials from step 3

### Manual Trigger

You can manually trigger the workflow at any time:
1. Go to: https://github.com/SmartAirTech/dns-domain-expiration-checker/actions
2. Click "Domain Expiration Check" workflow
3. Click "Run workflow" button

### Monitoring Domains

To add or remove domains:
1. Edit `smartair.txt`
2. Add one domain per line
3. Commit and push changes

### Troubleshooting

**No emails received?**
- Check GitHub Actions logs for errors
- Verify all secrets are configured correctly
- Check spam folder

**Workflow not running?**
- GitHub Actions are disabled by default on forked repos
- Enable them at: https://github.com/SmartAirTech/dns-domain-expiration-checker/actions
