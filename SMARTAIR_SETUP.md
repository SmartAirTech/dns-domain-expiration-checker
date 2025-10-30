# Smart Air Domain Monitoring Setup

## Automated Daily Email Notifications

This repository is configured to automatically check domain expiration dates daily and send email reports.

### GitHub Actions Workflow

The workflow runs daily at 9:00 AM UTC (5:00 PM Singapore Time) and checks all domains in `smartair.txt`.

### Required GitHub Secrets

To enable email notifications, configure these secrets in your GitHub repository:

1. Go to: https://github.com/SmartAirTech/dns-domain-expiration-checker/settings/secrets/actions
2. Click "New repository secret" and add each of the following:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `SMTP_SERVER` | Your email provider's SMTP server | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP port (usually 587 for TLS) | `587` |
| `SMTP_USERNAME` | Your email address | `your-email@gmail.com` |
| `SMTP_PASSWORD` | Your email password or app password | `your-app-password` |
| `EMAIL_FROM` | Sender email address | `alerts@smartair.com` |
| `EMAIL_TO` | Recipient email address(es) | `admin@smartair.com` |

### Gmail Configuration

If using Gmail:
1. Enable 2-factor authentication on your Google account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Use these settings:
   - `SMTP_SERVER`: `smtp.gmail.com`
   - `SMTP_PORT`: `587`
   - `SMTP_USERNAME`: Your Gmail address
   - `SMTP_PASSWORD`: The 16-character app password (no spaces)

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
