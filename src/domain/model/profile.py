from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime

@dataclass
class Profile:
    id: UUID
    email: str
    password: str
    created_at: datetime = field(default_factory=datetime.utcnow)

    def to_orm_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
        }