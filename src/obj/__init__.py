"""The `obj` module contains ABCs and Interface definitions for the application."""

from typing import Optional

from pydantic import BaseModel


class BaseRequest(BaseModel):
    id: int
    request: str
