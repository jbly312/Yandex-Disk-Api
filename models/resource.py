from datetime import datetime

from pydantic import BaseModel


class Resource(BaseModel):
    name: str
    path: str
    type: str
    created: datetime
    modified: datetime
    resource_id: str

    size: int | None = None
    md5: str | None = None
    mime_type: str | None = None
    public_url: str | None = None
    public_key: str | None = None

class FileResource(Resource):
    size: int     
    md5: str