#!/usr/bin/python3
import sys

def main():
    """Print only the command line arguments (excluding the script name)."""
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])

if __name__ == "__main__":
    main()
