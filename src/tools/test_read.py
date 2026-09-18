"""Test the read_file tool."""

from file_tools import read_file


def main():
    # We'll read the README.md that lives at the project root.
    # Note: we're running from src/tools, so we go up two levels.
    readme = read_file("../../README.md")
    print("--- Contents of README.md ---")
    print(readme)
    print("------------------------------")


if __name__ == "__main__":
    main()