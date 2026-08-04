from api.client import DiskClient
RESOURCES = "/v1/disk/resources"
TRASH = "/v1/disk/trash/resources"

class DiskApi:
    def __init__(self, client: DiskClient):
        self.client = client

    def get_disk_info(self):
        return self.client.get("/v1/disk")

    def create_folder(self, path: str):
        return self.client.put(
            RESOURCES, params={"path": path}
        )

    def get_meta(self, path: str, **params):
        return self.client.get(
            RESOURCES, params={"path": path, **params}
        )

    def delete(self, path: str, permanently: bool = True):
        return self.client.delete(
            RESOURCES, params={"path": path, "permanently": permanently}
        )

    def copy(self, source: str, destination: str, overwrite: bool = False):
        return self.client.post(
            f"{RESOURCES}/copy",
            params={"from": source, "path": destination, "overwrite": overwrite},
        )
    def move(self, source: str, destination: str, overwrite: bool = False):
        return self.client.post(
            f"{RESOURCES}/move",
            params={"from": source, "path": destination, "overwrite": overwrite},
        )
    def publish(self, path: str):
        return self.client.put(
            f"{RESOURCES}/publish",
            params={"path": path},
        )

    def get_trash(self, path: str = "/", **params):
        return self.client.get(TRASH, params={"path": path, **params})

    def restore_from_trash(self, path: str, name: str | None = None, overwrite: bool = False):
        params = {"path": path, "overwrite": overwrite}
        if name:
            params["name"] = name
        return self.client.put(f"{TRASH}/restore", params=params)

    def delete_from_trash(self, path: str | None = None):
        params = {"path": path} if path else {}
        return self.client.delete(TRASH, params=params)