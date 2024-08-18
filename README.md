# Feathercarver

Feathercarver is a Python tool designed to fix broken Markdown links in files. It can handle various types of Markdown links, including those with titles, and can process multiple files at once.

## Features

- Fixes broken Markdown links split across multiple lines
- Preserves code blocks and inline code
- Handles links with titles (both single and double quotes)
- Processes multiple files in a single run
- Maintains the original file structure and content outside of links

## Installation

To install Feathercarver, you can use pip:

```bash
pip install feathercarver
```

## Usage

You can use Feathercarver from the command line:

```bash
feathercarver file1.md file2.md file3.md
```

This will process all the specified Markdown files, fixing any broken links it finds.

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
