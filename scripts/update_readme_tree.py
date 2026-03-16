from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"

START_MARKER = "<!-- AUTO-TREE-START -->"
END_MARKER = "<!-- AUTO-TREE-END -->"

# Keep noisy/internal folders out of the README tree output.
EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".pytest_cache",
    ".vscode",
}


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in path.parts)


def iter_children(path: Path):
    children = [child for child in path.iterdir() if not should_skip(child)]
    return sorted(children, key=lambda p: (p.is_file(), p.name.lower()))


def build_tree(path: Path, prefix: str = "") -> list[str]:
    lines: list[str] = []
    children = iter_children(path)

    for index, child in enumerate(children):
        is_last = index == len(children) - 1
        branch = "└─ " if is_last else "├─ "
        lines.append(f"{prefix}{branch}{child.name}{'/' if child.is_dir() else ''}")

        if child.is_dir():
            extension = "   " if is_last else "│  "
            lines.extend(build_tree(child, prefix + extension))

    return lines


def make_auto_tree_block() -> str:
    lines = ["```text", f"{ROOT.name}/"]
    lines.extend(build_tree(ROOT))
    lines.append("```")
    return "\n".join(lines)


def update_readme() -> bool:
    readme = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in readme or END_MARKER not in readme:
        raise ValueError("README markers not found. Add AUTO-TREE-START/END markers.")

    start_index = readme.index(START_MARKER) + len(START_MARKER)
    end_index = readme.index(END_MARKER)

    block = "\n" + make_auto_tree_block() + "\n"
    updated = readme[:start_index] + block + readme[end_index:]

    if updated == readme:
        return False

    README_PATH.write_text(updated, encoding="utf-8")
    return True


if __name__ == "__main__":
    changed = update_readme()
    print("README updated" if changed else "README already up to date")
