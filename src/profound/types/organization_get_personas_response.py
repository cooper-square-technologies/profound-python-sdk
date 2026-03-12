# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OrganizationGetPersonasResponse",
    "Data",
    "DataCategory",
    "DataPersona",
    "DataPersonaBehavior",
    "DataPersonaDemographics",
    "DataPersonaEmployment",
]


class DataCategory(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str


class DataPersonaBehavior(BaseModel):
    motivations: Optional[str] = None

    pain_points: Optional[str] = FieldInfo(alias="painPoints", default=None)


class DataPersonaDemographics(BaseModel):
    age_range: Optional[List[str]] = FieldInfo(alias="ageRange", default=None)


class DataPersonaEmployment(BaseModel):
    company_size: Optional[List[str]] = FieldInfo(alias="companySize", default=None)

    industry: Optional[List[str]] = None

    job_title: Optional[List[str]] = FieldInfo(alias="jobTitle", default=None)

    role_seniority: Optional[List[str]] = FieldInfo(alias="roleSeniority", default=None)


class DataPersona(BaseModel):
    behavior: DataPersonaBehavior

    demographics: DataPersonaDemographics

    employment: DataPersonaEmployment


class Data(BaseModel):
    id: str

    category: DataCategory
    """Generic id+name reference used across domain boundaries."""

    name: str

    persona: DataPersona


class OrganizationGetPersonasResponse(BaseModel):
    data: List[Data]
