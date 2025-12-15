#!/bin/bash
# Install and configure gcloud SDK for podcast transcription system

set -e

echo "=== gcloud SDK Setup for Podcast Transcription System ==="
echo ""

# Detect OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

echo "Detected OS: $OS"
echo ""

# Check if gcloud is already installed
if command -v gcloud &> /dev/null; then
    echo "✓ gcloud is already installed"
    gcloud --version
    echo ""
    read -p "Reinstall anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Skipping installation"
        exit 0
    fi
fi

# Install gcloud SDK
echo "Installing gcloud SDK..."
echo ""

if [ "$OS" == "macOS" ]; then
    # macOS installation
    curl https://sdk.cloud.google.com | bash -s -- --disable-prompts --install-dir=$HOME

    # Add to PATH for current session
    export PATH="$HOME/google-cloud-sdk/bin:$PATH"

    # Add to shell profile
    if [ -f ~/.zshrc ]; then
        if ! grep -q "google-cloud-sdk/bin" ~/.zshrc; then
            echo 'export PATH="$HOME/google-cloud-sdk/bin:$PATH"' >> ~/.zshrc
            echo "✓ Added gcloud to ~/.zshrc"
        fi
    fi

elif [ "$OS" == "Linux" ]; then
    # Linux installation
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
    sudo apt-get update && sudo apt-get install google-cloud-sdk
fi

echo ""
echo "=== Installation Complete ==="
echo ""

# Verify installation
if command -v gcloud &> /dev/null; then
    echo "✓ gcloud installed successfully"
    gcloud --version
else
    echo "✓ gcloud installed at: ~/google-cloud-sdk/bin/gcloud"
    ~/google-cloud-sdk/bin/gcloud --version
fi

echo ""
echo "=== Next Steps ==="
echo ""
echo "1. Restart your terminal or run: source ~/.zshrc"
echo "2. Authenticate: gcloud auth login"
echo "3. Set project: gcloud config set project gen-lang-client-0111593271"
echo "4. Verify: gcloud config list"
echo ""
echo "Or run the interactive setup: gcloud init"
