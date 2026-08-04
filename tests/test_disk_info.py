class TestDiskInfo:

    def test_get_disk_info(self, disk_api):
        response = disk_api.get_disk_info()

        assert response.status_code == 200

    def test_disk_info_has_space_fields(self, disk_api):
        body = disk_api.get_disk_info().json()

        assert body["total_space"] > 0
        assert body["used_space"] <= body["total_space"]