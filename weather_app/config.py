"""Application configuration."""

import os
from dataclasses import dataclass
from pathlib import Path


OPENWEATHER_API_KEY_ENV = "OPENWEATHER_API_KEY"
DEFAULT_OPENWEATHER_API_KEY = "4c60d81d6fed58d57ba080a02e83681f"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOCAL_ENV_FILE = PROJECT_ROOT / ".env"


@dataclass(frozen=True)
class AppConfig:
    openweather_api_key: str


def load_app_config() -> AppConfig:
    """Load app configuration, falling back to the bundled public API key."""
    load_local_env_file()
    api_key = os.getenv(OPENWEATHER_API_KEY_ENV, DEFAULT_OPENWEATHER_API_KEY).strip()
    return AppConfig(openweather_api_key=api_key)


def load_local_env_file() -> None:
    """Load key=value pairs from .env without overriding real environment variables."""
    if not LOCAL_ENV_FILE.exists():
        return

    for line in LOCAL_ENV_FILE.read_text(encoding="utf-8").splitlines():
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith("#") or "=" not in stripped_line:
            continue

        key, value = stripped_line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
