"""PyInstaller build script."""
import subprocess
import sys

if __name__ == "__main__":
    subprocess.run(
        [sys.executable, "-m", "PyInstaller",
         "{{cookiecutter.project_slug}}.spec", "--noconfirm"],
        check=True,
    )
