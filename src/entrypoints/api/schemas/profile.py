from pydantic import BaseModel, ConfigDict, EmailStr, Field
from uuid import UUID
from datetime import datetime

class ProfileCreate(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

class ProfileRead(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"

class ProfileWithToken(BaseModel):
    profile: ProfileRead
    token: TokenResponse

class ProfileLogin(BaseModel):
    email: EmailStr
    password: str

class EmailUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr

class PasswordUpdate(BaseModel):
    old_password: str = Field(..., alias="oldPassword")
    new_password: str = Field(..., alias="newPassword")