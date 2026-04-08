# Multiprocessing Array Sort

A Python demo that uses `multiprocessing` to read, sort, and display a 12x12 integer array across three separate processes.

## How it works

1. Generates a random 12x12 matrix and writes it to `data.txt`
2. **Process A** reads the file into a shared list
3. **Process B** sorts all elements in ascending order
4. **Process C** prints the sorted matrix

## Usage

```bash
python main.py
```

Requires Python 3.6+.
