from pydantic import Field

from app.models.base import CamelModel


class AuthorizationVO(CamelModel):
    ak: str = Field(..., description="access token")
    token: str = Field(..., description="authorization token")
