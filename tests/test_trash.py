class TestTrash:

    def test_delete_moves_to_trash(self, disk_api, folder_path):
        disk_api.create_folder(folder_path)
        disk_api.delete(folder_path, permanently=False)

        assert disk_api.get_meta(folder_path).status_code == 404

        trash_items = disk_api.get_trash().json()["_embedded"]["items"]
        trashed = next(
            (item for item in trash_items if item["origin_path"] == f"disk:{folder_path}"),
            None,
        )

        assert trashed is not None

        disk_api.delete_from_trash(trashed["path"])

    def test_restore_from_trash(self, disk_api, folder_path):
        disk_api.create_folder(folder_path)
        disk_api.delete(folder_path, permanently=False)

        trash_items = disk_api.get_trash().json()["_embedded"]["items"]
        trashed = next(item for item in trash_items if item["origin_path"] == f"disk:{folder_path}")

        response = disk_api.restore_from_trash(trashed["path"])
        assert response.status_code == 201

        assert disk_api.get_meta(folder_path).status_code == 200
        disk_api.delete(folder_path, permanently=True)

    def test_permanent_delete_not_in_trash(self, disk_api, folder_path):
        disk_api.create_folder(folder_path)
        disk_api.delete(folder_path, permanently=True)

        trash_items = disk_api.get_trash().json()["_embedded"]["items"]
        trashed = next(
            (item for item in trash_items if item["origin_path"] == f"disk:{folder_path}"),
            None,
        )

        assert trashed is None