"""Entry point for {{cookiecutter.game_title}}."""
from src.{{cookiecutter.project_slug}}.game import GameWindow
import arcade


def main() -> None:
    GameWindow()
    arcade.run()


if __name__ == "__main__":
    main()
