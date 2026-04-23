"""Allow running as python -m {{cookiecutter.project_slug}}."""
from pathlib import Path
from agf.paths import set_project_root

set_project_root(Path(__file__).parents[3])  # src/<pkg>/__main__.py → project root

from src.{{cookiecutter.project_slug}}.game import main

main()
