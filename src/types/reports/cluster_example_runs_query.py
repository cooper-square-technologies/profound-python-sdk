# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ClusterExampleRunsQuery"]


class ClusterExampleRunsQuery(BaseModel):

    category_id: str

    cluster_id: str

    start_date: str

    end_date: str

    limit: Optional[int] = None

    offset: Optional[int] = None
