# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .persona_profile import PersonaProfile

__all__ = ["OrganizationGetPersonasResponse", "Data", "DataCategory", "DataOrganization"]


class DataCategory(BaseModel):
    id: str

    name: str


class DataOrganization(BaseModel):
    id: str

    name: Optional[str] = None


class Data(BaseModel):
    id: str

    category: DataCategory

    name: str

    organization: DataOrganization

    persona: PersonaProfile


class OrganizationGetPersonasResponse(BaseModel):
    data: List[Data]
