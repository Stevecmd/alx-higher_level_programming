#!/usr/bin/env python3
import os
import subprocess

def main():
    pyfile = os.environ.get('PYFILE')
    if not pyfile:
        print("Error: PYFILE environment variable is not set.")
        return

    if not os.path.exists(pyfile):
        print(f"Error: Python file '{pyfile}' not found.")
        return

    subprocess.run(['python3', pyfile])

if __name__ == "__main__":
    main()
