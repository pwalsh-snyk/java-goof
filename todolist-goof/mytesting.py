# test_snyk_code_detection.py

import os

def insecure_function():
    user_input = input("Enter a directory path: ")
    os.system(f"ls {user_input}")  # Command injection vulnerability

if __name__ == "__main__":
    insecure_function()

