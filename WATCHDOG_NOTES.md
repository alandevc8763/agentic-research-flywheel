# 🛠️ Watchdog Operational Notes

This file documents experiential findings and operational patterns discovered during autonomous Flywheel cycles.

## 🚩 Git Sync Pitfalls in Non-Interactive Environments

When running as a scheduled cron job, standard `git pull` or `git rebase` operations can hang or fail due to:
1. **Divergent Branches**: Remote and local branches having different histories.
2. **Merge Conflicts**: Automated updates to the same file (e.g., `curated_resources.md`) causing conflicts.
3. **Branch Naming**: Inconsistency between `main` and `master` across different repositories.

### 🛡️ The "Force-Sync" Pattern
To ensure atomic and non-blocking updates in a non-interactive session, use the following sequence:

```bash
# 1. Fetch latest state
git fetch origin

# 2. Force-reset to the target branch to clear any local divergence/conflicts
# IMPORTANT: Verify if the branch is 'main' or 'master'
git reset --hard origin/main 

# 3. Apply changes
# ... (append content, etc.) ...

# 4. Commit and Push
git add .
git commit -m "Autonomous update"
git push origin main
```

This pattern bypasses the need for interactive conflict resolution and ensures the agent always starts from the latest remote state.
