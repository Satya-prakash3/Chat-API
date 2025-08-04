import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
APPDIR = os.path.join(BASE_DIR, "chat")
ENV_DIR = os.path.join(BASE_DIR, ".env")

env = environ.Env()


env.read_env(ENV_DIR)


def get_settings() -> str:
    project_environment = env.str("PROJECT_ENVIRONMENT")
    if project_environment == "Production":
        settings_file = "ChatAPI.django.production"
    else:
        settings_file = "ChatAPI.django.base"
    return settings_file
    