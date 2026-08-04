import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")

BASE_URL = os.getenv("BASE_URL", "https://cloud-api.yandex.net")
TOKEN = os.getenv("YANDEX_DISK_TOKEN")
TEST_ROOT = "/autotests"

if not TOKEN:
    raise RuntimeError("YANDEX_DISK_TOKEN не задан. Скопируй .env.example в .env и заполни токен.")