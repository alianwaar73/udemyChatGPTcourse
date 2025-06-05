import os
import difflib

MAIN_README = "README.md"
MARKER_START = "<!-- AUTO-GENERATED-LIST:START -->"
MARKER_END = "<!-- AUTO-GENERATED-LIST:END -->"

def get_repo_files():
    result = []
    for root, dirs, files in os.walk("."):
        # Skip .git and .github
        if '.git' in root or '.github' in root:
            continue
        for f in files:
            if f == MAIN_README:
                continue
            path = os.path.relpath(os.path.join(root, f), ".")
            result.append(path)
    return sorted(result)

def get_sub_readmes():
    readmes = []
    for root, dirs, files in os.walk("."):
        if root == "." or '.git' in root or '.github' in root:
            continue
        for f in files:
            if f.lower() == "readme.md":
                path = os.path.relpath(os.path.join(root, f), ".")
                readmes.append(path)
    return sorted(readmes)

def update_main_readme():
    files = get_repo_files()
    sub_readmes = get_sub_readmes()
    if not os.path.exists(MAIN_README):
        print("No main README.md found.")
        return

    with open(MAIN_README, "r") as f:
        content = f.read()

    start = content.find(MARKER_START)
    end = content.find(MARKER_END)
    if start == -1 or end == -1:
        print("No marker found in main README. Add markers for auto section.")
        return

    new_section = "\n"
    new_section += "### Files in Repository\n\n"
    for f in files:
        new_section += f"- `{f}`\n"
    new_section += "\n### Sub-directory READMEs\n\n"
    for r in sub_readmes:
        new_section += f"- [{r}]({r})\n"
    new_section += "\n"

    new_content = (
        content[: start + len(MARKER_START)]
        + new_section
        + content[end:]
    )

    if new_content != content:
        with open(MAIN_README, "w") as f:
            f.write(new_content)
        print("README.md updated.")
    else:
        print("No changes detected in README.md.")

if __name__ == "__main__":
    update_main_readme()
