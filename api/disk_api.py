from api.client import DiskClient
RESOURCES = "/v1/disk/resources"


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