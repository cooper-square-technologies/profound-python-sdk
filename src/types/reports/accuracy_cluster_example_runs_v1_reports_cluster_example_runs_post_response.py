# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse", "ClusterExampleRun"]


class ClusterExampleRun(BaseModel):

    runId: str

    claim: str

    responseSnippet: str

    modelId: str

    regionId: str

    createdAt: str



class AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse(BaseModel):

    data: List[ClusterExampleRun]

    total_count: int = FieldInfo(alias="totalCount")
