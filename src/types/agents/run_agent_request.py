# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RunAgentRequest", "Inputs"]


class Inputs(BaseModel):
    pass



class RunAgentRequest(BaseModel):
    """Request body for starting an agent run."""

    inputs: Optional[Inputs] = None
    """Input values for the run. Keys should match the property names defined in `schema.input`. Omit the request body when the agent does not require inputs."""
