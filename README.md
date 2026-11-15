# Word Frequency Analyzer

Word Frequency Analyzer is a lightweight Python application that scans text files and calculates word frequencies.

The application normalizes words, removes punctuation, counts occurrences and exports the results into a report.

## Features

- Analyze plain text files
- Ignore punctuation
- Case-insensitive counting
- Sort by frequency
- Export results
- Summary statistics

## Example

Input

```
Rust is fast.
Python is popular.
Rust is reliable.
```

Output

```
is        3
rust      2
fast      1
python    1
popular   1
reliable  1
```

Run

```bash
python main.py
```
