# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PersonaProfileEmployment"]


class PersonaProfileEmployment(BaseModel):

    industry: Optional[List[str]] = None

    job_title: Optional[List[str]] = FieldInfo(alias="jobTitle", default=None)

    company_size: Optional[List[str]] = FieldInfo(alias="companySize", default=None)

    role_seniority: Optional[List[str]] = FieldInfo(alias="roleSeniority", default=None)
