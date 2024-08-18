__project_name__ = "feathercarver"
import argparse
import re
import sys
import typing


def fix_markdown_links(content):
    def replace_link(match):
        link_text = re.sub(r"\s+", " ", match.group("text").strip())
        url = re.sub(r"\s+", "", match.group("url").strip())
        return f"[{link_text}]({url})"

    pattern = re.compile(
        r"""
       \[
       (?P<text>
           [\s\S]*?
       )
       \]
       \s*
       \(
       (?P<url>
           [\s\S]*?
       )
       \)
   """,
        re.VERBOSE,
    )

    block_pattern = re.compile(
        r"""
       (?P<code>
           (?:
               ```[\s\S]*?```
               |
               `[^`\n]+?`
           )
       )
   """,
        re.VERBOSE,
    )

    blocks = block_pattern.split(content)

    for i in range(len(blocks)):
        if not block_pattern.match(blocks[i]):
            blocks[i] = pattern.sub(replace_link, blocks[i])

    return "".join(blocks)


def process_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()

        fixed_content = fix_markdown_links(content)

        with open(file_path, "w") as file:
            file.write(fixed_content)
        print(f"Processed {file_path}")
    except IOError as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)


def parse_arguments() -> typing.List[str]:
    parser = argparse.ArgumentParser(description="Fix broken Markdown links in paths.")
    parser.add_argument(
        "paths", nargs="+", help="One or more Markdown paths to process"
    )
    args = parser.parse_args()
    return list(dict.fromkeys(args.paths))


def main() -> int:
    file_paths = parse_arguments()

    for file_path in file_paths:
        process_file(file_path)

    return 0


__all__ = ["main"]
