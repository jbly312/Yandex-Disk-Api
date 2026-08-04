from pydantic import BaseModel


class DiskInfo(BaseModel):
    total_space: int
    used_space: int
    trash_size: int
    max_file_size: int
    revision: int