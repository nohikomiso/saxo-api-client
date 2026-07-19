"""Agent-facing guide shipped with the package (tool-agnostic)."""

from __future__ import annotations

from importlib.resources import files
from pathlib import Path

__all__ = ["read_guide", "write_guide"]


def read_guide() -> str:
    """Return the canonical agent GUIDE.md text."""
    return files(__package__).joinpath("GUIDE.md").read_text(encoding="utf-8")


def write_guide(destination: str | Path) -> Path:
    """Write GUIDE.md to destination (file or directory). Returns written path."""
    dest = Path(destination)
    if dest.exists() and dest.is_dir():
        dest = dest / "GUIDE.md"
    elif dest.suffix.lower() != ".md":
        dest = dest / "GUIDE.md" if not dest.suffix else dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(read_guide(), encoding="utf-8")
    return dest
