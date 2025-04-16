#!/usr/bin/env python3
import sys

max_word = None
max_count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    _, word, count = parts
    try:
        count = int(count)
    except ValueError:
        continue

    if count > max_count:
        max_count = count
        max_word = word

if max_word is not None:
    print(f"{max_word}\t{max_count}")
