# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .named_resource import NamedResource
from .persona_profile import PersonaProfile

__all__ = ["OrganizationGetPersonasResponse", "Data"]


class Data(BaseModel):
    id: str

    category: NamedResource
    """Generic id+name reference used across domain boundaries."""

    name: str

    persona: PersonaProfile


class OrganizationGetPersonasResponse(BaseModel):
    data: List[Data]
