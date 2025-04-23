#!/usr/bin/env python3
"""
Script to run code quality checks on the project.
"""

import subprocess
import sys

def run_command(command):
    """Run a command and return the exit code."""
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command)
    print()
    return result.returncode

def main():
    """Run all code quality checks."""
    print("Running code quality checks...\n")
    
    checks = [
        ["black", "--check", "."],
        ["isort", "--check", "."],
        ["flake8"],
        ["pytest"]
    ]
    
    failed = False
    for command in checks:
        exit_code = run_command(command)
        if exit_code != 0:
            failed = True
    
    if failed:
        print("Some checks failed!")
        sys.exit(1)
    else:
        print("All checks passed!")

if __name__ == "__main__":
    main()