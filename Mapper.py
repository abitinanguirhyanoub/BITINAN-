#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    word, count = line.split('\t', 1)
    print(f"most\t{word}\t{count}")
