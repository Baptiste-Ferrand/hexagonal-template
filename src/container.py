import os

from src.domain.lib.security import BcryptPasswordHasher
from src.domain.services.profile import ProfileService


class Container:
    def __init__(self, env: str | None = None):
        self.env = env if env is not None else os.getenv("ENV", "dev")
        self.hasher = BcryptPasswordHasher()

        if self.env in ("dev", "test"):
            from src.adapters.inmemory.repositories.profile import InMemoryProfileRepository
            self.profile_repo = InMemoryProfileRepository()
        else:
            from src.adapters.sqlalchemy.db import SessionLocal
            self.SessionFactory = SessionLocal

    def get_profile_service(self):
        if self.env in ("dev", "test"):
            repo = self.profile_repo
        else:
            from src.adapters.sqlalchemy.repositories.profile import SqlAlchemyProfileRepository
            session = self.SessionFactory()
            repo = SqlAlchemyProfileRepository(session)
        return ProfileService(repo, self.hasher)


container = Container()
