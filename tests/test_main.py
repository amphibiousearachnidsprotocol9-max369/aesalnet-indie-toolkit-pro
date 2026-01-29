import subprocess
import sys

def test_main_runs():
    result = subprocess.run(
        [sys.executable, "src/main.py", "--status"],
        capture_output=True,
        text=True,
    )
    assert "ONLINE" in result.stdout
