import uuid

import pytest

import config
from api.client import DiskClient
from api.disk_api import DiskApi


@pytest.fixture(scope="session")
def disk_api():
    return DiskApi(DiskClient(config.BASE_URL, config.TOKEN))


@pytest.fixture(scope="session", autouse=True)
def test_root(disk_api):

    disk_api.create_folder(config.TEST_ROOT)
    yield config.TEST_ROOT
    disk_api.delete(config.TEST_ROOT, permanently=True)


@pytest.fixture
def folder_path(test_root):
    return f"{test_root}/folder_{uuid.uuid4().hex[:8]}"


@pytest.fixture
def existing_folder(disk_api, folder_path):
    disk_api.create_folder(folder_path)
    yield folder_path
    disk_api.delete(folder_path, permanently=True)