from models.disk_info import DiskInfo

class TestDiskInfo:

    def test_get_disk_info(self, disk_api):
        response = disk_api.get_disk_info()

        assert response.status_code == 200

    def test_disk_info_schema(self, disk_api):
        info = DiskInfo(**disk_api.get_disk_info().json())

        assert info.total_space > 0
        assert info.used_space  <= info.total_space