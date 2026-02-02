import os
import sys

# Ensure the repository root is on sys.path so tests can import top-level modules
HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, os.pardir))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
