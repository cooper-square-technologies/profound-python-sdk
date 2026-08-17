# File generated from our OpenAPI spec by Scalar. See README.md for details.


from ..._models import BaseModel

__all__ = ["AccuracyTopicIdsQuery"]


class AccuracyTopicIdsQuery(BaseModel):

    category_id: str

    start_date: str

    end_date: str
