"""Configuration management for processor."""
import os
from google.cloud import secretmanager


class Config:
    """Configuration loaded from environment and secrets."""

    def __init__(
        self,
        anthropic_api_key: str,
        huggingface_token: str,
        github_token: str,
        gcs_bucket: str
    ):
        self.anthropic_api_key = anthropic_api_key
        self.huggingface_token = huggingface_token
        self.github_token = github_token
        self.gcs_bucket = gcs_bucket

    @classmethod
    def from_environment(cls):
        """Load configuration from environment variables and GCP secrets."""
        # Try environment variables first (for local testing)
        anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
        hf_token = os.environ.get("HUGGINGFACE_TOKEN")
        github_token = os.environ.get("GITHUB_TOKEN")

        # If not in env, try GCP Secret Manager (for Cloud Run)
        if not anthropic_key or not hf_token or not github_token:
            project_id = os.environ.get("GCP_PROJECT") or os.environ.get("GOOGLE_CLOUD_PROJECT")
            if project_id:
                client = secretmanager.SecretManagerServiceClient()

                if not anthropic_key:
                    anthropic_key = cls._get_secret(client, project_id, "ANTHROPIC_API_KEY")
                if not hf_token:
                    hf_token = cls._get_secret(client, project_id, "HUGGINGFACE_TOKEN")
                if not github_token:
                    github_token = cls._get_secret(client, project_id, "GITHUB_TOKEN")

        gcs_bucket = os.environ.get("GCS_BUCKET", "")

        if not all([anthropic_key, hf_token, github_token, gcs_bucket]):
            missing = []
            if not anthropic_key:
                missing.append("ANTHROPIC_API_KEY")
            if not hf_token:
                missing.append("HUGGINGFACE_TOKEN")
            if not github_token:
                missing.append("GITHUB_TOKEN")
            if not gcs_bucket:
                missing.append("GCS_BUCKET")
            raise ValueError(f"Missing required configuration: {', '.join(missing)}")

        return cls(
            anthropic_api_key=anthropic_key,
            huggingface_token=hf_token,
            github_token=github_token,
            gcs_bucket=gcs_bucket
        )

    @staticmethod
    def _get_secret(client, project_id: str, secret_name: str) -> str:
        """Get secret from GCP Secret Manager."""
        name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
