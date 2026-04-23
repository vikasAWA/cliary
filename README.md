# cliary

![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Type](https://img.shields.io/badge/type-CLI-lightgrey)

A minimal command-line journal for writing, reading, and searching notes.

## Installation

Using uv:

```
uv tool install .
```

For development:

```
uv pip install -e .
```

## Usage

Write notes:

```
cliary write
```

Enter text line by line. Type `exit` to finish.

Read today’s notes:

```
cliary read
```

Search notes:

```
cliary search <keyword>
```

## Storage

Notes are stored locally in the `logs/` directory.
Each day is saved as a separate file named by date.

## Requirements

* Python 3.8+
* uv (recommended)

## License

MIT

