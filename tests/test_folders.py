from models.resource import Resource
class TestFolders:

    def test_create_folder(self, disk_api, folder_path):
        response = disk_api.create_folder(folder_path)

        assert response.status_code == 201

        disk_api.delete(folder_path)

    def test_created_folder_is_dir(self, disk_api, existing_folder):
        body = disk_api.get_meta(existing_folder).json()
        resource = Resource(**body)

        assert resource.type == "dir"
        assert resource.path == f"disk:{existing_folder}"

    def test_create_duplicate(self, disk_api, existing_folder):
        response = disk_api.create_folder(existing_folder)
        assert response.status_code == 409

    def test_delete_folder(self, disk_api, folder_path):
        assert disk_api.create_folder(folder_path).status_code == 201

        response = disk_api.delete(folder_path)

        assert response.status_code == 204
        assert disk_api.get_meta(folder_path).status_code == 404