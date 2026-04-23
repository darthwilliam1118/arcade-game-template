"""Main game window for {{cookiecutter.game_title}}."""
from __future__ import annotations

import arcade
from agf.window import GameWindowBase

from src.{{cookiecutter.project_slug}}.game_config import GameConfig
from src.{{cookiecutter.project_slug}}.state import GameState, GameStateManager

SCREEN_TITLE = "{{cookiecutter.game_title}}"


class GameWindow(GameWindowBase):
    TITLE = SCREEN_TITLE

    def __init__(self) -> None:
        cfg = GameConfig.load()
        super().__init__(cfg, cfg.background, SCREEN_TITLE)

        # Fonts — add your TTF files to assets/fonts/ and load here
        # arcade.load_font(resource_path("assets/fonts/your_font.ttf"))

        self.music.set_volume(cfg.music_volume)

        self._manager = GameStateManager(self, GameState.SPLASH)
        self._manager.transition(GameState.SPLASH)


def main() -> None:
    GameWindow()
    arcade.run()
