# GCP Cloud Functions Deployment Skill

This is a Claude Code custom skill that enables automated deployment of Cloud Functions for the podcast transcription system.

## What This Skill Does

When you ask Claude to deploy or manage Google Cloud Functions, this skill automatically provides:
- Project-specific configuration (project ID, region, service accounts)
- Deployment commands for discovery and webhook functions
- Troubleshooting guidance
- Setup instructions for gcloud SDK

## File Structure

```
.claude/skills/gcp-cloud-functions/
├── SKILL.md              # Main skill definition (loaded by Claude)
├── setup-guide.md        # Detailed setup instructions
├── README.md             # This file
└── scripts/
    ├── deploy-all.sh     # Deploy all functions at once
    └── gcloud-setup.sh   # Install and configure gcloud SDK
```

## How It Works

Claude Code automatically discovers and loads this skill when you:
- Ask to deploy Cloud Functions
- Mention gcloud or GCP deployment
- Ask about serverless function management
- Need help with GCP authentication

The skill is **project-specific** and includes all the configuration for your podcast transcription system:
- Project ID: gen-lang-client-0111593271
- Service Account: podcast-processor@gen-lang-client-0111593271.iam.gserviceaccount.com
- Functions: discovery, email-reply-webhook
- Environment variables and secrets

## Usage Examples

Just ask Claude naturally:

```
Deploy the discovery function to GCP
```

```
Update the webhook function with my latest changes
```

```
Help me set up gcloud authentication
```

```
What's the status of my Cloud Functions?
```

Claude will automatically use this skill and apply the correct project configuration.

## Quick Commands

### Deploy All Functions
```bash
./.claude/skills/gcp-cloud-functions/scripts/deploy-all.sh
```

### Setup gcloud SDK
```bash
./.claude/skills/gcp-cloud-functions/scripts/gcloud-setup.sh
```

### Deploy Individual Function
See SKILL.md for specific deployment commands.

## Testing the Skill

After creating this skill, test it by asking Claude:
```
Can you deploy the discovery function?
```

Claude should automatically reference the project ID, region, and other settings from this skill without you having to provide them.

## Sharing with Team

This skill is stored in `.claude/skills/` which is part of your git repository. When you commit and push:

```bash
git add .claude/skills/gcp-cloud-functions/
git commit -m "Add GCP Cloud Functions deployment skill"
git push
```

Team members will automatically get this skill when they pull the latest changes!

## Customization

To modify the skill behavior, edit:
- **SKILL.md** - Main skill definition and quick reference
- **setup-guide.md** - Detailed setup documentation
- **scripts/** - Helper scripts for common tasks

## Learn More

- [Claude Code Skills Documentation](https://docs.anthropic.com/claude-code/skills)
- [Google Cloud Functions Documentation](https://cloud.google.com/functions/docs)
