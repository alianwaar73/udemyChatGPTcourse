# git-daily

`git-daily` is a simple, user-friendly shell script designed to provide a comprehensive daily snapshot of the current state of your local Git repository. It is useful for developers who want a quick, organized overview of their codebase before starting or ending their work session. The script fetches updates from remotes, displays the current status, visualizes recent commit history, and highlights any unstaged changes — all in a single command.

---

## What Does `git-daily` Do?

The script performs the following actions, in order:

1. **Fetches Latest Information from All Remotes:**
   - Runs `git fetch --all --prune` to update your local view of all remotes and clean up any references to deleted branches.

2. **Shows Working Directory Status:**
   - Runs `git status` to display untracked, changed, staged, and uncommitted files.

3. **Displays Recent Commit History:**
   - Uses `git log --graph --oneline --decorate --all --stat` to present a compact, visual graph of recent commits across all branches, including decorations (branch names, tags) and concise file change statistics.

4. **Lists Local Unstaged Changes:**
   - Runs `git diff` to show line-by-line differences for unstaged changes in your working directory.

5. **End of Overview:**
   - Prints a clear message indicating the end of the snapshot.

Each section is clearly separated by emojis and explanatory headers for readability.

---

## How to Install and Use `git-daily` Globally

To use `git-daily` from anywhere in your terminal as a simple command, follow these steps:

1. **Copy the Script:**
   - Save the script file as `git-daily` (no file extension is needed).

2. **Make the Script Executable:**
   ```bash
   chmod +x git-daily
   ```

3. **Move the Script to Your User's Local Bin Folder:**
   - This folder is typically included in your `PATH` by default.
   ```bash
   mv git-daily ~/.local/bin/
   ```

4. **Verify the Installation:**
   - Open a new terminal and run:
   ```bash
   git-daily
   ```
   - You should see the daily Git overview output in any directory that is a Git repository.

**Note:**  
If `~/.local/bin/` is not in your `PATH`, add it by appending this line to your `~/.bashrc` or `~/.zshrc`:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
Then reload your shell config:
```bash
source ~/.bashrc
# or
source ~/.zshrc
```

---

## When Should I Use `git-daily`?

Use this tool:
- At the start of your workday to get up-to-date with all branches and remotes.
- Before committing or pushing code, to double-check your working directory and recent changes.
- At the end of your session, to ensure you haven't left unstaged work or missed important changes.

---

## Limitations

- This script is meant for local, interactive use in Git repositories.
- It does **not** make any changes to your code or repository; it is read-only and non-destructive.
- The output is informational and may be verbose for very large repositories.

---

## Customization

Feel free to edit the script to display additional information (e.g., stashes, tags, branch summaries) or to tailor the output to your specific workflow.

---

> _This README was generated using Copilot's AI. The script is provided for educational and productivity purposes._