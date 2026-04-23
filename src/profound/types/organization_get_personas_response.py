# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .category import Category
from .organization import Organization
from .persona_profile import PersonaProfile

__all__ = ["OrganizationGetPersonasResponse", "Data"]


class Data(BaseModel):
    id: str

    category: Category

    name: str

    organization: Organization

    persona: PersonaProfile


class OrganizationGetPersonasResponse(BaseModel):
    data: List[Data]
