"""CLI entry point for {{name}}."""

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="{{name}}",
        description="{{description}}",
    )
    parser.add_argument("--name", default="world", help="Name to greet")
    args = parser.parse_args(argv)

    from src.core import hello

    print(hello(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
