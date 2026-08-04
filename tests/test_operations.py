class TestCopyMove:
    def test_copy_folder(self, disk_api, destination_path,existing_folder):
        response = disk_api.copy(existing_folder,destination_path)
        assert response.status_code == 201

        disk_api.delete(destination_path)

    def test_copy_keeps_source(self, disk_api, existing_folder, destination_path):
        assert disk_api.copy(existing_folder, destination_path).status_code == 201

        assert disk_api.get_meta(existing_folder).status_code == 200
        assert disk_api.get_meta(destination_path).status_code == 200
        disk_api.delete(destination_path)

    def test_move_removes_source(self, disk_api, existing_folder, destination_path):
        assert disk_api.move(existing_folder, destination_path).status_code == 201

        assert disk_api.get_meta(existing_folder).status_code == 404
        assert disk_api.get_meta(destination_path).status_code == 200

    def test_copy_to_existing_path(self, disk_api, existing_folder, destination_path):
        assert disk_api.copy(existing_folder, destination_path).status_code == 201
        assert disk_api.copy(existing_folder, destination_path).status_code == 409

        disk_api.delete(destination_path)