# {{cookiecutter.game_title}} — Claude Code Guidelines

## Project structure
- src/{{cookiecutter.project_slug}}/ — game source code
- assets/                — images, fonts, sounds (not committed if empty)
- tests/                 — pytest tests
- game_config.toml       — user-editable config
- main.py                — entry point

## Framework dependency
agf (arcade-game-framework) is installed as a dependency.
Source: https://github.com/darthwilliam1118/arcade-game-framework
Version: {{cookiecutter.agf_version}}
Import as: from agf.paths import resource_path

Do NOT re-implement anything already in agf.

## Key agf modules
- agf.paths.resource_path()    — PyInstaller-safe asset loading
- agf.background               — StaticBackground, ProceduralStarField
- agf.events.GameEvent         — base game events
- agf.high_scores              — HighScoreTable persistence
- agf.music.MusicPlayer        — music management
- agf.levels.base_level        — BaseLevel abstract interface
- agf.powerups                 — PowerUpManager, effect categories
- agf.ui                       — HUDBase, ScorePopup, text_utils
- agf.views                    — base view classes (subclass these)
- agf.state                    — BaseGameStateManager (subclassed in state.py)
- agf.window                   — GameWindowBase (subclassed in game.py)

## Where to add game logic
- src/{{cookiecutter.project_slug}}/levels/  — add new level types here
- src/{{cookiecutter.project_slug}}/sprites/ — add player/enemy sprites here
- src/{{cookiecutter.project_slug}}/views/run_level.py — main gameplay view
- Replace PlaceholderLevel in level_factory.py with real level types

## Arcade version
Arcade 3.3.x. Key rules:
- Use self.clear() not arcade.start_render()
- Use arcade.Text objects, never arcade.draw_text() in on_draw()
- Load fonts before creating Text objects
- SpriteList.update() requires delta_time parameter in 3.x
- Never use bold=True unless the TTF has a bold variant
- All assets via resource_path() for PyInstaller compatibility

## Testing
- pytest --cov=src
- All tests must run without a display
- Inject textures/sounds as constructor parameters for testability

## Code style
- Python {{cookiecutter.python_version}}+
- Type hints on all public methods
- Black formatting, Ruff linting
- Commit via terminal to trigger pre-commit hooks (not VS Code UI)

## Build
- python build.py → produces dist/{{cookiecutter.project_slug}}.exe
- PyInstaller bundles agf automatically via site-packages
