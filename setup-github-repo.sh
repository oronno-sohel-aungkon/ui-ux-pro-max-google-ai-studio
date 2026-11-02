#!/usr/bin/env bash
set -e

echo "======================================================================"
echo "   UI/UX Pro Max - GitHub Repository Publisher for Google AI Studio"
echo "======================================================================"
echo ""

read -p "Enter your GitHub Repository URL (e.g., https://github.com/username/ui-ux-pro-max-google-ai-studio.git): " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "[!] No URL entered. Aborting."
    exit 1
fi

echo ""
echo "[*] Initializing Git repository..."
git init

echo "[*] Staging all files..."
git add .

echo "[*] Committing files..."
git commit -m "feat: Initial commit of UI/UX Pro Max for Google AI Studio"

echo "[*] Renaming default branch to main..."
git branch -M main

echo "[*] Setting remote origin to $REPO_URL..."
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"

echo "[*] Pushing to GitHub..."
git push -u origin main

echo ""
echo "======================================================================"
echo "[SUCCESS] Your repository is now live on GitHub!"
echo "Anyone can now install it to Google AI Studio directly from your repo."
echo "======================================================================"
