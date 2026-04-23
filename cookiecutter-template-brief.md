# Project: arcade-game-template (Cookiecutter)

## Overview
Create a cookiecutter project template repo that generates a fully
runnable stub game using the agf package. The generated project launches,
shows a splash screen, cycles through a main menu (leaderboard +
instructions), and has a placeholder run_level view. All infrastructure
is wired and working. The game developer replaces the placeholder level
with real game logic.

This brief is for the TEMPLATE repo itself — not a generated game.
Claude Code creates the template files with {{cookiecutter.variable}}
placeholders throughout. The template repo lives at:
  github.com/darthwilliam1118/arcade-game-template
The repo is cloned locally here in the current directory
files for arcade-game-framework (agf) are cloned locally at: C:\Users\darth\Code\arcade-game-framework 
any discrepancy between this brief and the agf source files use the agf source as ground truth.

## agf package structure (for reference)
agf is installed as a dependency. Its modules are:
  agf.background        — StaticBackground, ProceduralStarField
  agf.config            — BaseGameConfig, config_path
  agf.events            — GameEvent
  agf.high_scores       — HighScoreTable, scores_path
  agf.levels.base_level — BaseLevel
  agf.music             — MusicPlayer
  agf.paths             — resource_path
  agf.player_state      — PlayerState
  agf.powerups          — PowerUpManager, PowerUpSpawner, effect categories
  agf.spawn_safety      — apply_spawn_safety
  agf.sprites           — ExplosionSprite, ParticleEmitter, ShockwaveSprite
  agf.state             — BaseGameStateManager
  agf.ui                — HUDBase, ScorePopup, text_utils, FONT_MAIN, FONT_THIN
  agf.views             — SplashView, MainMenuView, GameOverView,
                          ScoreEntryView, LevelCompleteView
                          (no PlayerKilledView in agf — implement standalone)
  agf.window            — GameWindowBase

---

## Template repo structure

```
arcade-game-template/
├── cookiecutter.json
├── README.md                          ← explains how to use the template
├── .gitignore                         ← ignore __pycache__, *.pyc etc
└── {{cookiecutter.project_slug}}/     ← everything inside here is generated
    ├── .github/
    │   └── workflows/
    │       └── build.yml
    ├── .gitattributes
    ├── .gitignore
    ├── .pre-commit-config.yml
    ├── CLAUDE.md
    ├── LICENSE
    ├── README.md
    ├── pyproject.toml
    ├── game_config.toml
    ├── {{cookiecutter.project_slug}}.spec
    ├── build.py
    ├── main.py
    ├── assets/
    │   ├── fonts/
    │   │   └── .gitkeep
    │   ├── images/
    │   │   └── .gitkeep
    │   └── sounds/
    │       └── .gitkeep
    ├── src/
    │   └── {{cookiecutter.project_slug}}/
    │       ├── __init__.py
    │       ├── __main__.py
    │       ├── game.py
    │       ├── game_config.py
    │       ├── game_event.py
    │       ├── state.py
    │       ├── levels/
    │       │   ├── __init__.py
    │       │   ├── base_level.py
    │       │   ├── level_factory.py
    │       │   └── placeholder_level.py
    │       ├── sprites/
    │       │   ├── __init__.py
    │       │   └── player_ship.py
    │       ├── ui/
    │       │   ├── __init__.py
    │       │   └── hud.py
    │       └── views/
    │           ├── __init__.py
    │           ├── splash.py
    │           ├── main_menu.py
    │           ├── run_level.py
    │           ├── player_killed.py
    │           ├── level_complete.py
    │           ├── game_over.py
    │           └── score_entry.py
    └── tests/
        ├── __init__.py
        └── test_smoke.py
```

---

## cookiecutter.json

```json
{
    "project_name": "My Arcade Game",
    "project_slug": "my_arcade_game",
    "game_title": "My Arcade Game",
    "author_name": "Your Name",
    "github_username": "yourusername",
    "python_version": "3.14",
    "agf_version": "v0.1.0",
    "window_height": 800,
    "aspect_ratio": "1.25",
    "num_lives": 3,
    "starting_level": 1
}
```

`project_slug` is used in import paths, package name, and exe name.
It must be snake_case. Users should set it manually if project_name
contains spaces (cookiecutter does not auto-slugify).

---

## File contents — each file below is a template file

All Python imports use `{{cookiecutter.project_slug}}` as the package
name. All display strings use `{{cookiecutter.game_title}}`. All author
references use `{{cookiecutter.author_name}}`.

### cookiecutter.json — already shown above

### README.md (template root — explains the template itself)

```markdown
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
python -m venv venv
venv\Scripts\activate        # Windows
pip install -e ".[dev]"
python main.py               # should launch immediately
```

Replace `src/your_slug/levels/placeholder_level.py` with your game logic.
```

### {{cookiecutter.project_slug}}/README.md

```markdown
# {{cookiecutter.game_title}}

A 2D arcade game built with Python and
[Arcade](https://api.arcade.academy/) using the
[arcade-game-framework](https://github.com/darthwilliam1118/arcade-game-framework).

## Running

Download the latest release exe from the Releases page, or run from source:

```bash
python -m venv venv
venv\Scripts\activate
pip install -e ".[dev]"
python main.py
```

## Development

```bash
pip install -e ".[dev]"
pytest --cov=src
black .
ruff check .
```

## License

MIT — see LICENSE.
```

### {{cookiecutter.project_slug}}/LICENSE

```
MIT License

Copyright (c) 2026 {{cookiecutter.author_name}}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### {{cookiecutter.project_slug}}/pyproject.toml

```toml
[project]
name = "{{cookiecutter.project_slug}}"
version = "0.1.0"
requires-python = ">={{cookiecutter.python_version}}"
dependencies = [
    "arcade>=3.3.3,<4.0",
    "arcade-game-framework @ git+https://github.com/darthwilliam1118/arcade-game-framework@{{cookiecutter.agf_version}}",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov",
    "ruff",
    "black",
    "cookiecutter",
]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 100

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.backends.legacy:build"

[tool.setuptools.packages.find]
where = ["src"]
```

### {{cookiecutter.project_slug}}/game_config.toml

```toml
[game]
starting_level = {{cookiecutter.starting_level}}
num_lives = {{cookiecutter.num_lives}}
music_volume = 80
effects_volume = 80
debug = false
god_mode = false
max_window_height = {{cookiecutter.window_height}}
sprite_scale = 1.0

[background]
background_image = "assets/images/background.png"
star_count = 300
star_speed_min = 20.0
star_speed_max = 120.0

[ui]
popup_duration = 0.8
popup_rise_speed = 60.0
```

### {{cookiecutter.project_slug}}/.gitattributes

```
* text=auto
*.py text eol=lf
*.toml text eol=lf
*.yml text eol=lf
*.md text eol=lf
*.json text eol=lf
*.cfg text eol=lf
*.txt text eol=lf
*.spec text eol=lf
```

### {{cookiecutter.project_slug}}/.pre-commit-config.yml

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.4
    hooks:
      - id: ruff
```

### {{cookiecutter.project_slug}}/.github/workflows/build.yml

```yaml
name: CI / Build

on:
  push:
    branches: [main]
    tags: ["v*"]
  workflow_dispatch:

permissions:
  contents: write

jobs:
  test-and-build:
    runs-on: windows-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "{{cookiecutter.python_version}}"
          cache: "pip"

      - name: Install dependencies
        run: pip install -e ".[dev]"

      - name: Lint
        run: |
          black --check .
          ruff check .

      - name: Run tests
        run: pytest --cov=src

      - name: Build exe
        run: python build.py

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: {{cookiecutter.game_title}}-windows
          path: dist/{{cookiecutter.project_slug}}.exe
          if-no-files-found: error

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        if: startsWith(github.ref, 'refs/tags/')
        with:
          files: |
            dist/{{cookiecutter.project_slug}}.exe
            game_config.toml
```

### {{cookiecutter.project_slug}}/build.py

```python
"""PyInstaller build script."""
import subprocess
import sys

if __name__ == "__main__":
    subprocess.run(
        [sys.executable, "-m", "PyInstaller",
         "{{cookiecutter.project_slug}}.spec", "--noconfirm"],
        check=True,
    )
```

### {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}.spec

```python
# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

block_cipher = None

a = Analysis(
    ["main.py"],
    pathex=[str(Path("src"))],
    binaries=[],
    datas=[
        ("assets", "assets"),
        ("game_config.toml", "."),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="{{cookiecutter.project_slug}}",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

### {{cookiecutter.project_slug}}/main.py

```python
"""Entry point for {{cookiecutter.game_title}}."""
from src.{{cookiecutter.project_slug}}.game import GameWindow
import arcade


def main() -> None:
    GameWindow()
    arcade.run()


if __name__ == "__main__":
    main()
```

### src/{{cookiecutter.project_slug}}/__init__.py

```python
"""{{cookiecutter.game_title}}."""
```

### src/{{cookiecutter.project_slug}}/__main__.py

```python
"""Allow running as python -m {{cookiecutter.project_slug}}."""
from src.{{cookiecutter.project_slug}}.game import main

main()
```

### src/{{cookiecutter.project_slug}}/game_event.py

```python
"""Game events — re-exports agf base events."""
from agf.events import GameEvent

__all__ = ["GameEvent"]
```

### src/{{cookiecutter.project_slug}}/game_config.py

```python
"""Game configuration — extends agf BaseGameConfig."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from agf.background.background_config import BackgroundConfig
from agf.config.base_config import BaseGameConfig, config_path
from agf.ui.ui_config import UIConfig


@dataclass
class GameConfig(BaseGameConfig):
    background: BackgroundConfig = None  # type: ignore[assignment]
    ui: UIConfig = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.background is None:
            self.background = BackgroundConfig()
        if self.ui is None:
            self.ui = UIConfig()

    @classmethod
    def load(cls, path: Optional[Path] = None) -> "GameConfig":
        if path is None:
            path = config_path()
        try:
            with open(path, "rb") as fh:
                data = tomllib.load(fh)
        except Exception:
            return cls()

        game = data.get("game", {})
        bg_raw = data.get("background", {})
        ui_raw = data.get("ui", {})

        bg = BackgroundConfig(
            background_image=str(
                bg_raw.get("background_image", BackgroundConfig.background_image)
            ),
            star_count=int(bg_raw.get("star_count", BackgroundConfig.star_count)),
            star_speed_min=float(
                bg_raw.get("star_speed_min", BackgroundConfig.star_speed_min)
            ),
            star_speed_max=float(
                bg_raw.get("star_speed_max", BackgroundConfig.star_speed_max)
            ),
        )
        ui = UIConfig(
            popup_duration=float(
                ui_raw.get("popup_duration", UIConfig.popup_duration)
            ),
            popup_rise_speed=float(
                ui_raw.get("popup_rise_speed", UIConfig.popup_rise_speed)
            ),
        )
        return cls(
            starting_level=int(game.get("starting_level", cls.starting_level)),
            num_lives=int(game.get("num_lives", cls.num_lives)),
            music_volume=int(game.get("music_volume", cls.music_volume)),
            effects_volume=int(game.get("effects_volume", cls.effects_volume)),
            debug=bool(game.get("debug", cls.debug)),
            god_mode=bool(game.get("god_mode", cls.god_mode)),
            max_window_height=int(
                game.get("max_window_height", cls.max_window_height)
            ),
            sprite_scale=float(game.get("sprite_scale", cls.sprite_scale)),
            background=bg,
            ui=ui,
        )

    def save(self, path: Optional[Path] = None) -> None:
        if path is None:
            path = config_path()
        bg = self.background
        lines = [
            "[game]\n",
            f"starting_level = {self.starting_level}\n",
            f"num_lives = {self.num_lives}\n",
            f"music_volume = {self.music_volume}\n",
            f"effects_volume = {self.effects_volume}\n",
            f"debug = {'true' if self.debug else 'false'}\n",
            f"god_mode = {'true' if self.god_mode else 'false'}\n",
            f"max_window_height = {self.max_window_height}\n",
            f"sprite_scale = {self.sprite_scale}\n",
            "\n[background]\n",
            f'background_image = "{bg.background_image}"\n',
            f"star_count = {bg.star_count}\n",
            f"star_speed_min = {bg.star_speed_min}\n",
            f"star_speed_max = {bg.star_speed_max}\n",
        ]
        path.write_text("".join(lines), encoding="utf-8")
```

### src/{{cookiecutter.project_slug}}/state.py

```python
"""GameStateManager for {{cookiecutter.game_title}}."""
from __future__ import annotations

import logging
from enum import Enum, auto
from typing import TYPE_CHECKING, Any

from agf.state import BaseGameStateManager

if TYPE_CHECKING:
    import arcade

log = logging.getLogger(__name__)


class GameState(Enum):
    SPLASH = auto()
    MAIN = auto()
    GAME_INIT = auto()
    SET_ACTIVE_PLAYER = auto()
    START_LEVEL = auto()
    RUN_LEVEL = auto()
    LEVEL_COMPLETE = auto()
    PLAYER_KILLED = auto()
    GAME_OVER = auto()
    SCORE_ENTRY = auto()
    EXIT = auto()


class GameStateManager(BaseGameStateManager):

    def _enter_state(self, state: GameState) -> None:
        from src.{{cookiecutter.project_slug}}.views.splash import SplashView
        from src.{{cookiecutter.project_slug}}.views.main_menu import MainMenuView
        from src.{{cookiecutter.project_slug}}.views.run_level import RunLevelView
        from src.{{cookiecutter.project_slug}}.views.level_complete import LevelCompleteView
        from src.{{cookiecutter.project_slug}}.views.player_killed import PlayerKilledView
        from src.{{cookiecutter.project_slug}}.views.game_over import GameOverView
        from src.{{cookiecutter.project_slug}}.views.score_entry import ScoreEntryView

        match state:
            case GameState.SPLASH:
                self.window.show_view(SplashView(self))
            case GameState.MAIN:
                self.window.show_view(MainMenuView(self))
            case GameState.GAME_INIT:
                self._handle_game_init()
            case GameState.SET_ACTIVE_PLAYER:
                self._handle_set_active_player()
            case GameState.START_LEVEL:
                self._handle_start_level()
            case GameState.RUN_LEVEL:
                self.window.show_view(RunLevelView(self))
            case GameState.LEVEL_COMPLETE:
                self.window.show_view(LevelCompleteView(self))
            case GameState.PLAYER_KILLED:
                self.window.show_view(PlayerKilledView(self))
            case GameState.GAME_OVER:
                self.window.show_view(GameOverView(self))
            case GameState.SCORE_ENTRY:
                self.window.show_view(ScoreEntryView(self))
            case GameState.EXIT:
                import arcade
                arcade.exit()

    def _handle_game_init(self) -> None:
        from agf.player_state import PlayerState
        from src.{{cookiecutter.project_slug}}.game_config import GameConfig

        cfg = self.context.get("config") or GameConfig.load()
        num_players = self.context.get("num_players", 1)
        self.context["config"] = cfg
        self.context["players"] = [
            PlayerState(
                player_num=i + 1,
                lives=cfg.num_lives,
                current_level=cfg.starting_level,
            )
            for i in range(num_players)
        ]
        self.context["active_player_index"] = 0
        self.transition(GameState.SET_ACTIVE_PLAYER)

    def _handle_set_active_player(self) -> None:
        self.transition(GameState.START_LEVEL)

    def _handle_start_level(self) -> None:
        from src.{{cookiecutter.project_slug}}.levels.level_factory import create_level

        players = self.context.get("players", [])
        idx = self.context.get("active_player_index", 0)
        cfg = self.context.get("config")
        level_number = players[idx].current_level if players else 1
        snapshot = players[idx].level_snapshot if players else None

        level = create_level(
            level_number=level_number,
            config=cfg,
            window_width=self.window.width,
            window_height=self.window.height,
            snapshot=snapshot,
        )
        self.context["current_level"] = level
        self.transition(GameState.RUN_LEVEL)
```

### src/{{cookiecutter.project_slug}}/game.py

```python
"""Main game window for {{cookiecutter.game_title}}."""
from __future__ import annotations

import arcade
from agf.background.star_field import ProceduralStarField
from agf.background.static_background import StaticBackground
from agf.music import MusicPlayer
from agf.paths import resource_path
from agf.window import GameWindowBase

from src.{{cookiecutter.project_slug}}.game_config import GameConfig
from src.{{cookiecutter.project_slug}}.state import GameState, GameStateManager

SCREEN_TITLE = "{{cookiecutter.game_title}}"


class GameWindow(GameWindowBase):
    TITLE = SCREEN_TITLE

    def __init__(self) -> None:
        cfg = GameConfig.load()
        super().__init__(cfg)

        # Fonts — add your TTF files to assets/fonts/ and load here
        # arcade.load_font(resource_path("assets/fonts/your_font.ttf"))

        bg = cfg.background
        self.background = StaticBackground(bg.background_image,
                                           self.width, self.height)
        self.star_field = ProceduralStarField(
            self.width, self.height,
            bg.star_count, bg.star_speed_min, bg.star_speed_max,
        )
        self.music = MusicPlayer()
        self.music.set_volume(cfg.music_volume)

        self._manager = GameStateManager(self)
        self._manager.transition(GameState.SPLASH)


def main() -> None:
    GameWindow()
    arcade.run()
```

### src/{{cookiecutter.project_slug}}/levels/__init__.py

Empty.

### src/{{cookiecutter.project_slug}}/levels/base_level.py

```python
"""Re-exports agf BaseLevel for use within this package."""
from agf.levels.base_level import BaseLevel

__all__ = ["BaseLevel"]
```

### src/{{cookiecutter.project_slug}}/levels/placeholder_level.py

```python
"""PlaceholderLevel — stub level shown until real game logic is added.

Replace this file with your game's level implementation.
See agf.levels.base_level.BaseLevel for the full interface.
"""
from __future__ import annotations

from typing import Any
import arcade
from agf.levels.base_level import BaseLevel
from agf.game_event import GameEvent


class PlaceholderLevel(BaseLevel):
    """A do-nothing level that never clears.

    Shows a centered message and lets the player press W to win
    or L to lose for testing purposes.
    """

    def __init__(self, window_width: int, window_height: int):
        self._w = window_width
        self._h = window_height
        self._label = arcade.Text(
            "REPLACE THIS WITH YOUR GAME LOGIC\n"
            "W = win level   L = lose a life",
            x=window_width / 2,
            y=window_height / 2,
            color=arcade.color.WHITE,
            font_size=18,
            anchor_x="center",
            anchor_y="center",
            multiline=True,
            width=window_width - 80,
            align="center",
        )

    @property
    def level_type(self) -> str:
        return "placeholder"

    def setup(self, level_number: int) -> None:
        pass

    def update(self, delta_time: float,
               player_ship: Any) -> list[GameEvent]:
        return []

    def draw(self) -> None:
        self._label.draw()

    def is_cleared(self) -> bool:
        return False

    def apply_player_bullet(self, bullet: Any) -> Any:
        return None

    def consume_pending_hits(self) -> list[tuple[float, float, int]]:
        return []

    def consume_pending_non_lethal_hits(self) -> list[tuple[float, float]]:
        return []

    def get_all_enemy_sprites(self) -> arcade.SpriteList:
        return arcade.SpriteList()

    def get_enemy_bullet_sprite_list(self) -> arcade.SpriteList:
        return arcade.SpriteList()

    def get_powerup_manager(self):
        return None

    def to_snapshot(self) -> dict:
        return {"level_type": "placeholder"}

    @classmethod
    def from_snapshot(cls, snapshot: dict, config: Any,
                      window_width: int,
                      window_height: int) -> "PlaceholderLevel":
        return cls(window_width, window_height)
```

### src/{{cookiecutter.project_slug}}/levels/level_factory.py

```python
"""LevelFactory — maps level number to BaseLevel instance."""
from __future__ import annotations

from typing import Any
from agf.levels.base_level import BaseLevel


def create_level(level_number: int, config: Any,
                 window_width: int, window_height: int,
                 snapshot: dict | None = None) -> BaseLevel:
    """Create or restore a level.

    Replace the placeholder case with your game's level types.
    """
    if snapshot is not None:
        return _restore(snapshot, config, window_width, window_height)
    return _create_fresh(level_number, config, window_width, window_height)


def _create_fresh(level_number: int, config: Any,
                  window_width: int,
                  window_height: int) -> BaseLevel:
    from src.{{cookiecutter.project_slug}}.levels.placeholder_level import (
        PlaceholderLevel,
    )
    # TODO: replace with real level types
    # e.g. if level_number % 5 == 0: return BossLevel(...)
    level = PlaceholderLevel(window_width, window_height)
    level.setup(level_number)
    return level


def _restore(snapshot: dict, config: Any,
             window_width: int,
             window_height: int) -> BaseLevel:
    from src.{{cookiecutter.project_slug}}.levels.placeholder_level import (
        PlaceholderLevel,
    )
    level_type = snapshot.get("level_type", "placeholder")
    match level_type:
        case "placeholder":
            return PlaceholderLevel.from_snapshot(
                snapshot, config, window_width, window_height
            )
        case _:
            raise ValueError(f"Unknown level type: {level_type!r}")
```

### src/{{cookiecutter.project_slug}}/sprites/__init__.py

Empty.

### src/{{cookiecutter.project_slug}}/sprites/player_ship.py

```python
"""Placeholder player ship sprite.

Replace with your game's actual player ship implementation.
"""
from __future__ import annotations

import arcade


class PlayerShip(arcade.Sprite):
    """Simple placeholder ship — a colored rectangle.

    Replace with a real sprite loaded from assets/images/.
    """

    def __init__(self, window_width: int, window_height: int,
                 scale: float = 1.0):
        super().__init__()
        # Placeholder texture — replace with arcade.load_texture(...)
        self.texture = arcade.make_soft_circle_texture(
            40, arcade.color.CYAN
        )
        self.scale = scale
        self._window_width = window_width
        self._window_height = window_height

        # Spawn at centre bottom
        self.center_x = window_width / 2
        self.center_y = 60

        self.hit_points: int = 100
        self.max_hit_points: int = 100

    def is_invincible(self) -> bool:
        return False

    def take_damage(self, amount: int) -> bool:
        self.hit_points = max(0, self.hit_points - amount)
        return self.hit_points <= 0

    def apply_movement(self, keys_held: set[int],
                       delta_time: float) -> None:
        speed = 300.0
        if arcade.key.LEFT in keys_held or arcade.key.A in keys_held:
            self.center_x -= speed * delta_time
        if arcade.key.RIGHT in keys_held or arcade.key.D in keys_held:
            self.center_x += speed * delta_time
        # Clamp to window
        half = self.width / 2
        self.center_x = max(half,
                            min(self._window_width - half, self.center_x))

    def update(self, delta_time: float = 1 / 60) -> None:
        pass
```

### src/{{cookiecutter.project_slug}}/ui/__init__.py

Empty.

### src/{{cookiecutter.project_slug}}/ui/hud.py

```python
"""HUD for {{cookiecutter.game_title}}."""
from __future__ import annotations

from typing import Optional
import arcade
from agf.ui.hud_base import HUDBase
from agf.ui.text_utils import FONT_MAIN, FONT_THIN


class HUD(HUDBase):

    def __init__(self, window_width: int, window_height: int,
                 num_players: int = 1):
        super().__init__(window_width, window_height)
        self._num_players = num_players
        self._score_text: Optional[arcade.Text] = None
        self._lives_text: Optional[arcade.Text] = None
        self._level_text: Optional[arcade.Text] = None
        self._last_score = -1
        self._last_lives = -1
        self._last_level = -1
        self._build()

    def _build(self) -> None:
        w, h = self.window_width, self.window_height
        y = h - 24
        self._score_text = arcade.Text(
            "SCORE: 0", 16, y,
            arcade.color.WHITE, 16,
            font_name=FONT_MAIN, anchor_y="center",
        )
        self._lives_text = arcade.Text(
            "LIVES: 3", w - 16, y,
            arcade.color.WHITE, 16,
            font_name=FONT_MAIN,
            anchor_x="right", anchor_y="center",
        )
        self._level_text = arcade.Text(
            "LEVEL: 1", w / 2, y,
            arcade.color.WHITE, 16,
            font_name=FONT_MAIN,
            anchor_x="center", anchor_y="center",
        )

    def update(self, players: list, active_idx: int,
               level: int) -> None:
        if not players:
            return
        p = players[active_idx]
        if p.score != self._last_score:
            self._last_score = p.score
            if self._score_text:
                self._score_text.text = f"SCORE: {p.score}"
        if p.lives != self._last_lives:
            self._last_lives = p.lives
            if self._lives_text:
                self._lives_text.text = f"LIVES: {p.lives}"
        if level != self._last_level:
            self._last_level = level
            if self._level_text:
                self._level_text.text = f"LEVEL: {level}"

    def draw(self) -> None:
        if self._score_text:
            self._score_text.draw()
        if self._lives_text:
            self._lives_text.draw()
        if self._level_text:
            self._level_text.draw()
```

### src/{{cookiecutter.project_slug}}/views/__init__.py

Empty.

### src/{{cookiecutter.project_slug}}/views/splash.py

```python
"""Splash screen for {{cookiecutter.game_title}}."""
from __future__ import annotations

from typing import TYPE_CHECKING
from agf.views.splash import SplashView as _AGFSplash

if TYPE_CHECKING:
    from src.{{cookiecutter.project_slug}}.state import GameStateManager


class SplashView(_AGFSplash):
    TITLE = "{{cookiecutter.game_title}}"
    AUTO_ADVANCE = 5.0

    def __init__(self, manager: "GameStateManager") -> None:
        self._manager = manager
        super().__init__(on_complete=self._go_to_main)

    def _preload_tracks(self) -> None:
        # Load music tracks here, e.g.:
        # self.window.music.load_track("menu")
        # self.window.music.load_track("level_1")
        self._assets_ready = True  # remove this line once tracks added

    def _go_to_main(self) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState
        self._manager.transition(GameState.MAIN)
```

### src/{{cookiecutter.project_slug}}/views/main_menu.py

```python
"""Main menu for {{cookiecutter.game_title}}."""
from __future__ import annotations

from typing import TYPE_CHECKING
from agf.views.main_menu import MainMenuView as _AGFMainMenu

if TYPE_CHECKING:
    from src.{{cookiecutter.project_slug}}.state import GameStateManager


class MainMenuView(_AGFMainMenu):

    def __init__(self, manager: "GameStateManager") -> None:
        super().__init__()
        self._manager = manager

    def music_track(self) -> str:
        return "menu"  # update once you add a menu music track

    def on_start_1p(self) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState
        cfg = self._manager.context.get("config")
        self._manager.transition(GameState.GAME_INIT,
                                  num_players=1, config=cfg)

    def on_start_2p(self) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState
        cfg = self._manager.context.get("config")
        self._manager.transition(GameState.GAME_INIT,
                                  num_players=2, config=cfg)

    def on_config(self) -> None:
        pass  # add a config view when ready

    def on_exit(self) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState
        self._manager.transition(GameState.EXIT)
```

### src/{{cookiecutter.project_slug}}/views/run_level.py

```python
"""RunLevelView — active gameplay screen.

This is a minimal stub. Replace PlaceholderLevel in level_factory.py
with your real level implementation and extend this view as needed.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import arcade
from agf.ui.text_utils import FONT_MAIN

if TYPE_CHECKING:
    from src.{{cookiecutter.project_slug}}.state import GameStateManager


class RunLevelView(arcade.View):

    def __init__(self, manager: "GameStateManager") -> None:
        super().__init__()
        self._manager = manager
        self._keys_held: set[int] = set()
        self._level = None
        self._ship = None
        self._ship_list = arcade.SpriteList()
        self._hud = None
        self._paused = False
        self._setup()

    def _setup(self) -> None:
        from src.{{cookiecutter.project_slug}}.sprites.player_ship import PlayerShip
        from src.{{cookiecutter.project_slug}}.ui.hud import HUD

        ctx = self._manager.context
        cfg = ctx.get("config")
        scale = cfg.sprite_scale if cfg else 1.0

        self._level = ctx.get("current_level")
        self._ship = PlayerShip(
            self.window.width, self.window.height, scale=scale
        )
        self._ship_list.append(self._ship)
        players = ctx.get("players", [])
        self._hud = HUD(self.window.width, self.window.height,
                        len(players))

    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time: float) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState

        delta_time = min(delta_time, 1 / 15)
        self.window.star_field.update(delta_time)

        if self._paused:
            return

        if self._ship:
            self._ship.apply_movement(self._keys_held, delta_time)
            self._ship.update(delta_time)

        if self._level:
            events = self._level.update(delta_time, self._ship)
            for event in events:
                from agf.events import GameEvent
                if event == GameEvent.LEVEL_COMPLETE:
                    self._manager.transition(GameState.LEVEL_COMPLETE)
                    return
                elif event == GameEvent.PLAYER_KILLED:
                    self._manager.transition(GameState.PLAYER_KILLED)
                    return

        ctx = self._manager.context
        players = ctx.get("players", [])
        idx = ctx.get("active_player_index", 0)
        level_num = players[idx].current_level if players else 1
        if self._hud:
            self._hud.update(players, idx, level_num)

    def on_draw(self) -> None:
        self.clear()
        self.window.background.draw()
        self.window.star_field.draw()

        if self._level:
            self._level.draw()

        self._ship_list.draw()

        if self._hud:
            self._hud.draw()

        if self._paused:
            w, h = self.window.width, self.window.height
            arcade.draw_lrbt_rectangle_filled(0, w, 0, h, (0, 0, 0, 140))
            arcade.draw_text(
                "PAUSED",
                w / 2, h / 2,
                arcade.color.WHITE, 48,
                font_name=FONT_MAIN,
                anchor_x="center", anchor_y="center",
            )

    def on_key_press(self, key: int, modifiers: int) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState

        if key == arcade.key.P:
            self._paused = not self._paused
            return

        # Debug shortcuts — remove when real level is implemented
        if key == arcade.key.W and (modifiers & arcade.key.MOD_SHIFT):
            self._manager.transition(GameState.LEVEL_COMPLETE)
            return
        if key == arcade.key.L:
            self._manager.transition(GameState.PLAYER_KILLED)
            return

        self._keys_held.add(key)

    def on_key_release(self, key: int, modifiers: int) -> None:
        self._keys_held.discard(key)
```

### src/{{cookiecutter.project_slug}}/views/player_killed.py

```python
"""PlayerKilledView — brief pause after player death.

No agf base class — self-contained implementation.
"""
from __future__ import annotations

import math
from typing import TYPE_CHECKING, Optional
import arcade
from agf.ui.text_utils import FONT_MAIN, centered_text

if TYPE_CHECKING:
    from src.{{cookiecutter.project_slug}}.state import GameStateManager

_DISPLAY_DURATION = 2.0


class PlayerKilledView(arcade.View):

    def __init__(self, manager: "GameStateManager") -> None:
        super().__init__()
        self._manager = manager
        self._elapsed: float = 0.0
        self._label: Optional[arcade.Text] = None

    def on_show_view(self) -> None:
        w, h = self.window.width, self.window.height
        self._label = centered_text(
            "SHIP DESTROYED",
            w, h // 2,
            font_size=36,
            color=arcade.color.RED,
            font_name=FONT_MAIN,
        )

    def on_update(self, delta_time: float) -> None:
        self.window.star_field.update(delta_time)
        self._elapsed += delta_time
        if self._elapsed >= _DISPLAY_DURATION:
            self._advance()

    def on_draw(self) -> None:
        self.clear()
        self.window.background.draw()
        self.window.star_field.draw()
        if self._label:
            alpha = int(abs(math.sin(self._elapsed * 3)) * 255)
            self._label.color = (255, 60, 60, alpha)
            self._label.draw()

    def on_key_press(self, key: int, modifiers: int) -> None:
        self._advance()

    def _advance(self) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState
        players = self._manager.context.get("players", [])
        idx = self._manager.context.get("active_player_index", 0)
        if players:
            players[idx].lives -= 1
        if not players or players[idx].lives <= 0:
            self._manager.transition(GameState.GAME_OVER)
        else:
            self._manager.transition(GameState.SET_ACTIVE_PLAYER)
```

### src/{{cookiecutter.project_slug}}/views/level_complete.py

```python
"""LevelCompleteView."""
from __future__ import annotations

from typing import TYPE_CHECKING
from agf.views.level_complete import LevelCompleteView as _AGFLevelComplete

if TYPE_CHECKING:
    from src.{{cookiecutter.project_slug}}.state import GameStateManager


class LevelCompleteView(_AGFLevelComplete):

    def __init__(self, manager: "GameStateManager") -> None:
        self._manager = manager
        super().__init__(on_complete=self._on_complete)

    def _on_complete(self) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState
        players = self._manager.context.get("players", [])
        idx = self._manager.context.get("active_player_index", 0)
        if players:
            players[idx].current_level += 1
            players[idx].level_snapshot = None
        self._manager.transition(GameState.SET_ACTIVE_PLAYER)
```

### src/{{cookiecutter.project_slug}}/views/game_over.py

```python
"""GameOverView."""
from __future__ import annotations

from typing import TYPE_CHECKING
from agf.views.game_over import GameOverView as _AGFGameOver

if TYPE_CHECKING:
    from src.{{cookiecutter.project_slug}}.state import GameStateManager


class GameOverView(_AGFGameOver):

    def __init__(self, manager: "GameStateManager") -> None:
        self._manager = manager
        super().__init__(on_complete=self._on_complete)

    def _on_complete(self) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState
        self._manager.transition(GameState.SCORE_ENTRY)
```

### src/{{cookiecutter.project_slug}}/views/score_entry.py

```python
"""ScoreEntryView."""
from __future__ import annotations

from typing import TYPE_CHECKING
from agf.views.score_entry import ScoreEntryView as _AGFScoreEntry

if TYPE_CHECKING:
    from src.{{cookiecutter.project_slug}}.state import GameStateManager


class ScoreEntryView(_AGFScoreEntry):

    def __init__(self, manager: "GameStateManager") -> None:
        self._manager = manager
        super().__init__(on_complete=self._on_complete)

    def _on_complete(self) -> None:
        from src.{{cookiecutter.project_slug}}.state import GameState
        self._manager.transition(GameState.MAIN)
```

### tests/__init__.py

Empty.

### tests/test_smoke.py

```python
"""Smoke tests — confirm basic imports and config load without a display."""


def test_agf_importable() -> None:
    import agf
    assert hasattr(agf, "__version__")


def test_game_config_loads() -> None:
    from src.{{cookiecutter.project_slug}}.game_config import GameConfig
    cfg = GameConfig.load()
    assert cfg.num_lives > 0
    assert cfg.starting_level >= 1


def test_game_event_importable() -> None:
    from src.{{cookiecutter.project_slug}}.game_event import GameEvent
    from agf.events import GameEvent as AGFEvent
    assert GameEvent is AGFEvent


def test_state_importable() -> None:
    from src.{{cookiecutter.project_slug}}.state import GameState, GameStateManager
    assert GameState.SPLASH is not None


def test_placeholder_level() -> None:
    from src.{{cookiecutter.project_slug}}.levels.placeholder_level import (
        PlaceholderLevel,
    )
    level = PlaceholderLevel(800, 600)
    assert level.level_type == "placeholder"
    assert not level.is_cleared()
    assert level.consume_pending_hits() == []
```

---

## CLAUDE.md for generated projects

```markdown
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
```

---

## Implementation notes for Claude Code

- Every file in the `{{cookiecutter.project_slug}}/` directory tree must
  use `{{cookiecutter.variable}}` syntax for all game-specific strings.
  Test by searching for hardcoded "my_arcade_game" strings — there
  should be none.

- The template repo itself has no Python source to run. Do not attempt
  to `pip install` or run the template — it only makes sense after
  cookiecutter generates a project from it.

- The `agf.views` base classes (SplashView, MainMenuViewBase, etc.)
  must exist in agf before this template can be validated. The template
  assumes these exist with `on_complete` callback pattern. If agf views
  use a different pattern, update the generated view subclasses to match.

- `PlayerKilledViewBase`, `LevelCompleteViewBase`, `GameOverViewBase`,
  `ScoreEntryViewBase` are referenced in the generated views. These
  must exist in agf. If they don't yet, create simple stubs in agf first
  that accept an `on_complete` callable and call it after a brief delay
  (PlayerKilled: 1.5s, LevelComplete: 2s, GameOver: 3s, ScoreEntry:
  immediately on key press).

- The background.png referenced in game_config.toml does not exist in
  the template assets. This is intentional — the game developer adds
  their own. The StaticBackground class handles missing files gracefully
  by falling back to a solid color. Verify this is the case in agf
  before finalising the template.

- Do not add any Kenney assets to the template — it ships with empty
  asset folders only. Game developers bring their own assets.
```
