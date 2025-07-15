from typing import TypedDict
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.domain.lib.jwt_manager import decode_access_token, TokenExpiredError, TokenInvalidError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:

    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    try:
        payload = decode_access_token(token)
        return payload
    except TokenExpiredError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except TokenInvalidError as e:
        raise HTTPException(status_code=401, detail=str(e))

class UserPayload(TypedDict):
    sub: str
    roles: "list[str]"

def require_owner_profile(current_user: dict = Depends(get_current_user), profile_id: str | None = None):
    if not profile_id:
        raise HTTPException(status_code=400, detail="Profile ID is required")
    
    if current_user.get("sub") != profile_id:
        raise HTTPException(status_code=403, detail="You do not have permission to access this profile")
    
    return current_user