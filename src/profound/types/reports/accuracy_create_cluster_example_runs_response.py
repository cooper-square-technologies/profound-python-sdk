# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateClusterExampleRunsResponse", "Data"]


class Data(BaseModel):
    claim: str

    created_at: str = FieldInfo(alias="createdAt")

    api_model_id: str = FieldInfo(alias="modelId")

    region_id: str = FieldInfo(alias="regionId")

    response_snippet: str = FieldInfo(alias="responseSnippet")

    run_id: str = FieldInfo(alias="runId")


class AccuracyCreateClusterExampleRunsResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
