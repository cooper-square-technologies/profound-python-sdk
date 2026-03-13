# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PersonaProfileEmployment"]


class PersonaProfileEmployment(BaseModel):
    company_size: Optional[List[str]] = FieldInfo(alias="companySize", default=None)

    industry: Optional[List[str]] = None

    job_title: Optional[List[str]] = FieldInfo(alias="jobTitle", default=None)

    role_seniority: Optional[List[str]] = FieldInfo(alias="roleSeniority", default=None)
