# 📦 Git Repository Setup

## ✅ Local Repository Initialized

Your local git repository has been initialized and your first commit has been created!

## 🔗 Push to Remote Repository

To push your code to a remote repository (GitHub, GitLab, etc.), follow these steps:

### Option 1: GitHub (Recommended)

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Name it: `HomeHunter` or `wyszukiwarka-mieszkan`
   - Choose Public or Private
   - **Don't** initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

2. **Connect and push:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

### Option 2: GitLab

1. **Create a new project on GitLab:**
   - Go to https://gitlab.com/projects/new
   - Name it and create the project

2. **Connect and push:**
   ```bash
   git remote add origin https://gitlab.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

### Option 3: Custom Remote

If you already have a remote repository URL:

```bash
git remote add origin YOUR_REMOTE_URL
git branch -M main
git push -u origin main
```

## 🔐 Authentication

For HTTPS, you may need to authenticate:
- **GitHub:** Use Personal Access Token (PAT) instead of password
- **GitLab:** Use Personal Access Token
- **SSH:** If using SSH URLs, make sure your SSH key is set up

## 📝 Useful Git Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# Add new changes
git add .
git commit -m "Your commit message"

# Push updates
git push

# View remotes
git remote -v
```

## 🚫 What's Ignored

The `.gitignore` file ensures these are NOT committed:
- `*.db` - Database files
- `__pycache__/` - Python cache
- `venv/` - Virtual environments
- `.streamlit/` - Streamlit config
- `dist/` - Build artifacts
- `*.app` - macOS apps

---

Your code is ready to be pushed! 🚀

