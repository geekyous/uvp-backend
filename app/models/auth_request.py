from pydantic import BaseModel


class AuthRequest(BaseModel):
    sk: str
    ak: str
