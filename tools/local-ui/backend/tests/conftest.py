import sys
from pathlib import Path

# Ensure backend package is importable when tests run directly
sys.path.append(str(Path(__file__).resolve().parents[2]))
