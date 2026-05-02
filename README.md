# arcade-game-template

Cookiecutter template for Python arcade games built on the
[arcade-game-framework](https://github.com/darthwilliam1118/arcade-game-framework).

## Usage

```bash
pip install cookiecutter
cookiecutter gh:darthwilliam1118/arcade-game-template
```

Answer the prompts and a new project folder is generated, ready to run.

## What you get

- Working splash screen, main menu (leaderboard + instructions),
  game over, and score entry views
- Placeholder run_level view with a simple ship sprite
- High score persistence
- Scrolling star field background
- PyInstaller build pipeline
- GitHub Actions CI (lint + test + build exe)
- Pre-commit hooks (Black + Ruff)

## After generating

```bash
cd your_project_slug
git init && git add -A && git commit -m "Initial commit from template"
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -e ".[dev]"
python main.py               # use "python" not "py" — py bypasses the venv on Windows
```

Replace `src/your_slug/levels/placeholder_level.py` with your game logic.
