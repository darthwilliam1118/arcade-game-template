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
