# Feathercarver

Feathercarver is a Python tool designed to fix broken Markdown links in files. It can handle various types of Markdown links, including those with titles, and can process multiple files or directories at once.

## Features

- Fixes broken Markdown links split across multiple lines
- Preserves code blocks and inline code
- Handles links with titles (both single and double quotes)
- Processes multiple files or directories in a single run
- Maintains the original file structure and content outside of links

## Installation

To install Feathercarver, you can use pip:

```bash
pip install feathercarver
```

## Usage

Feathercarver supports two main subcommands: `processfiles` and `processdirs`.

### Processing Individual Files

To process individual files, use the `processfiles` subcommand:

```bash
feathercarver processfiles file1.md file2.md file3.md
```

This will process all the specified Markdown files, fixing any broken links it finds.

### Processing Directories

To process entire directories, use the `processdirs` subcommand:

```bash
feathercarver processdirs path/to/directory1 path/to/directory2
```

By default, this will process all `.md` files in the specified directories and their subdirectories.

You can specify which file extensions to process using the `--ext` option:

```bash
feathercarver processdirs path/to/directory --ext md txt
```

This will process both `.md` and `.txt` files in the specified directory although this 
link checker was meant to process only markdown files.

### Verbosity

You can increase the verbosity of the output using the `-v` or `--verbose` option:

```bash
feathercarver -v processfiles file1.md
feathercarver -vv processdirs path/to/directory
```

Use `-v` for info-level logging, `-vv` for debug-level logging, and `-vvv` for the most detailed logging.

## Development

To set up the development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/gkwa/feathercarver.git
   cd feathercarver
   ```

2. Install dependencies:
   ```bash
   rye sync
   . .venv/bin/activate
   ```

3. Run tests:
   ```bash
   pytest
   ```
