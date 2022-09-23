import pytest
from django.conf import settings
import environ
from pathlib import Path

@pytest.fixture(scope='session')
def django_db_setup():
    ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
    APPS_DIR = ROOT_DIR / "bot_xsmb"
    env = environ.Env()
    READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
    if READ_DOT_ENV_FILE:
        env.read_env(str(ROOT_DIR / ".env"))
    settings.DATABASES["default"] = env.db("DATABASE_URL")  # noqa F405
    settings.DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
    settings.DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405


# from bot_xsmb.users.models import User
# from bot_xsmb.users.tests.factories import UserFactory


# @pytest.fixture(autouse=True)
# def media_storage(settings, tmpdir):
#     settings.MEDIA_ROOT = tmpdir.strpath


# @pytest.fixture
# def user() -> User:
#     return UserFactory()