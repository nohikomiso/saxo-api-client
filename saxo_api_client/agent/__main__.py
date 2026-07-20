"""CLI: print or write the agent GUIDE (any AI tool)."""

from __future__ import annotations

import argparse
import sys

from saxo_api_client import __version__
from saxo_api_client.agent import read_guide, write_guide


def main(argv: list[str] | None = None) -> int:
    argv_list = list(sys.argv[1:] if argv is None else argv)
    # Bare invocation (esp. `python -m saxo_api_client.agent`) prints the guide.
    if not argv_list:
        argv_list = ["agent-guide"]

    parser = argparse.ArgumentParser(
        prog="saxo-api-client",
        description="saxo-api-client utilities for humans and AI agents",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"saxo-api-client {__version__}",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    guide = sub.add_parser(
        "agent-guide",
        help="Print the canonical agent GUIDE.md (or write it to a path)",
    )
    guide.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        help="Write GUIDE.md to PATH (file or directory) instead of stdout",
    )

    args = parser.parse_args(argv_list)

    if args.command == "agent-guide":
        if args.output:
            path = write_guide(args.output)
            print(f"Wrote {path}", file=sys.stderr)
        else:
            text = read_guide()
            sys.stdout.write(text if text.endswith("\n") else text + "\n")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
