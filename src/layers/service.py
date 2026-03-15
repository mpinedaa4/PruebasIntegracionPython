
from typing import Optional
from .repository import InMemoryUserRepository

class UserService:
    def __init__(self, repo: InMemoryUserRepository):
        self.repo = repo

    def get_full_name(self, user_id: int) -> Optional[str]:
        u = self.repo.find_by_id(user_id)
        return None if u is None else f"{u.first} {u.last}"
