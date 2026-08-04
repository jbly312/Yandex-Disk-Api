class TestFolders:

    def test_create_folder_returns_201(self, disk_api, folder_path):
        response = disk_api.create_folder(folder_path)

        assert response.status_code == 201

        disk_api.delete(folder_path)

    def test_created_folder_is_dir(self, disk_api, existing_folder):
        body = disk_api.get_meta(existing_folder).json()

        assert body["type"] == "dir"
        assert body["path"] == f"disk:{existing_folder}"

    def test_create_duplicate_returns_409(self, disk_api, existing_folder):
        # TODO: повторный create_folder на тот же путь
        ...

    def test_delete_folder_returns_204(self, disk_api, folder_path):
        # TODO: создать папку, удалить, проверить код
        ...