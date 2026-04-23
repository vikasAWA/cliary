# cliary

![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Type](https://img.shields.io/badge/type-CLI-lightgrey)

A minimal command-line journal for writing, reading, and searching notes.

Notes are automatically grouped by day — each day gets its own file.

---

## Installation

```id="z9r3xk"
uv tool install cliary
```

---

## Quick Example

```id="f2v6ny"
$ cliary write
>> today I learned about pathlib
>> built my first CLI tool
>> exit
Saved. Exiting...
```

```id="3r5yhl"
$ cliary read

today I learned about pathlib
built my first CLI tool
```

```id="6x8pqm"
$ cliary search good

2026-04-23.txt: weather is good today

```

---

## Usage

Write notes:

```id="h1k9vb"
cliary write
```

Read today’s notes:

```id="q7n2dj"
cliary read
```

Search notes:

```id="m4w8rs"
cliary search <keyword>
```

---

## Storage

Notes are stored in a `logs/` directory in the current working folder.

Example:

```id="b2k6lm"
project/
 ├── logs/
 │    ├── 2026-04-23.txt
```

Each day creates a new file.

---

## Requirements

* Python 3.8+

---

## License

MIT

