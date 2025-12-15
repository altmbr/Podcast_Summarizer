"""Git operations for pushing processed episodes."""
from pathlib import Path
from git import Repo
import subprocess


class GitRepo:
    """Git repository wrapper."""

    def __init__(self, path: Path):
        self.path = path
        self.repo = Repo(path)

    @classmethod
    def clone(cls, repo_url: str, path: Path):
        """Clone repository."""
        print(f"Cloning repository to {path}...")
        path.parent.mkdir(parents=True, exist_ok=True)
        Repo.clone_from(repo_url, path)
        print(f"✓ Repository cloned")
        return cls(path)

    def add_all(self):
        """Stage all changes."""
        print("Staging changes...")
        self.repo.git.add(A=True)

    def commit(self, message: str):
        """Commit changes."""
        print(f"Committing: {message[:50]}...")
        self.repo.index.commit(message)
        print("✓ Changes committed")

    def push(self):
        """Push to origin."""
        print("Pushing to GitHub...")
        origin = self.repo.remote(name="origin")
        origin.push()
        print("✓ Pushed to GitHub")
