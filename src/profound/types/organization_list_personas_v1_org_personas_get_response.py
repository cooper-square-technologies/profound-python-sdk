# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .organization import Organization

__all__ = [
    "OrganizationListPersonasV1OrgPersonasGetResponse",
    "Data",
    "DataPersona",
    "DataPersonaBehavior",
    "DataPersonaEmployment",
    "DataPersonaDemographics",
    "DataCategory",
]


class DataCategory(BaseModel):
    id: str

    name: str

    internal_name: Optional[str] = None


class DataPersonaDemographics(BaseModel):
    age_range: Optional[List[str]] = FieldInfo(alias="ageRange", default=None)


class DataPersonaEmployment(BaseModel):
    industry: Optional[List[str]] = None

    job_title: Optional[List[str]] = FieldInfo(alias="jobTitle", default=None)

    company_size: Optional[List[str]] = FieldInfo(alias="companySize", default=None)

    role_seniority: Optional[List[str]] = FieldInfo(alias="roleSeniority", default=None)


class DataPersonaBehavior(BaseModel):
    pain_points: Optional[str] = FieldInfo(alias="painPoints", default=None)

    motivations: Optional[str] = None


class DataPersona(BaseModel):
    behavior: DataPersonaBehavior

    employment: DataPersonaEmployment

    demographics: DataPersonaDemographics


class Data(BaseModel):
    id: str

    name: str

    persona: DataPersona

    category: DataCategory

    organization: Organization


class OrganizationListPersonasV1OrgPersonasGetResponse(BaseModel):
    data: List[Data]
