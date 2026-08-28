# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateClusterExampleRunsResponse", "Data"]


class Data(BaseModel):
    run_id: str = FieldInfo(alias="runId")

    claim: str

    response_snippet: str = FieldInfo(alias="responseSnippet")

    api_model_id: str = FieldInfo(alias="modelId")

    region_id: str = FieldInfo(alias="regionId")

    created_at: str = FieldInfo(alias="createdAt")


class AccuracyCreateClusterExampleRunsResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
