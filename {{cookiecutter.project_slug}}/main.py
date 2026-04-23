"""Entry point for {{cookiecutter.game_title}}."""
from pathlib import Path
from agf.paths import set_project_root

set_project_root(Path(__file__).parent)

from src.{{cookiecutter.project_slug}}.game import GameWindow
import arcade


def main() -> None:
    GameWindow()
    arcade.run()


if __name__ == "__main__":
    main()
