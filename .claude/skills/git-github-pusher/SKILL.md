---
name: git-github-pusher
description: Automates the process of initializing a local Git repository, handling remote conflicts, and pushing code to GitHub. Trigger when the user mentions "push", "上傳github", "push to github", or asks to upload/push their code to an upstream repository.
---

# Git & GitHub Pusher Skill

This skill automates the workflow for pushing local changes to a remote GitHub repository. Use it whenever a user wants to upload their local project to GitHub.

## Workflow Execution Steps

When triggered, carefully follow these sequential steps to reliably push the local code to the user's remote repository:

### 1. Check Git Status & Initialize
- Check if the current directory is a git repository using `git status`.
- If it is not a git repository, initialize it (`git init`), add all files (`git add .`), and create an initial commit (`git commit -m "Initial commit"`).
- If it is already initialized but has uncommitted changes, add and commit them (`git add . && git commit -m "Update"`) before pushing.

### 2. Verify Remote & Ask User (If Needed)
- Check existing remotes using `git remote -v`.
- If no remote named `origin` exists, instruct the user to create an empty repository on GitHub and provide the remote URL (e.g., `https://github.com/username/repo.git` or SSH equivalent). Pause and wait for the user to provide the URL.
- Once the user provides the URL, add the remote (`git remote add origin <URL>`).

### 3. Handle Remote Conflicts & Unrelated Histories
- Ensure you are pushing to the `main` branch: `git branch -M main`.
- To safely handle situations where the remote repository was initialized with a README or LICENSE file, always attempt to pull changes first using:
  `git pull origin main --no-rebase --allow-unrelated-histories`
- If merge conflicts occur (e.g., in `README.md`), use your file editing tools to view and resolve them by keeping the local content intact or properly merging it.
- If conflicts were resolved, commit the resolved state (`git add . && git commit -m "Resolve merge conflicts"`).

### 4. Push to Remote
- Execute the push command: `git push -u origin main`.
- Confirm via `command_status` that the push was successful.
- Inform the user that the push is complete and provide the final GitHub repository URL.
