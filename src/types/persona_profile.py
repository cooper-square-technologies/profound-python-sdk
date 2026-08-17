# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel
from .persona_profile_behavior import PersonaProfileBehavior
from .persona_profile_employment import PersonaProfileEmployment
from .persona_profile_demographics import PersonaProfileDemographics

__all__ = ["PersonaProfile"]


class PersonaProfile(BaseModel):

    behavior: PersonaProfileBehavior

    employment: PersonaProfileEmployment

    demographics: PersonaProfileDemographics
