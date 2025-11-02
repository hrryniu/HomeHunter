#!/bin/bash
# Instructions to push HaWooPa Hunter to GitHub
# Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual values

echo "🔗 Setting up remote and pushing to GitHub..."
echo ""
echo "Step 1: Create a new repository on GitHub at https://github.com/new"
echo "        Name it: HaWooPa-Hunter (or wyszukiwarka-mieszkan)"
echo "        Don't initialize with README, .gitignore, or license"
echo ""
read -p "Press Enter after you've created the repository..."

echo ""
echo "Step 2: Enter your GitHub username:"
read -p "Username: " GITHUB_USER

echo ""
echo "Step 3: Enter your repository name:"
read -p "Repository name: " REPO_NAME

echo ""
echo "Setting up remote..."
git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git
git branch -M main

echo ""
echo "Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Done! Your code has been pushed to GitHub."
echo "   View it at: https://github.com/$GITHUB_USER/$REPO_NAME"

