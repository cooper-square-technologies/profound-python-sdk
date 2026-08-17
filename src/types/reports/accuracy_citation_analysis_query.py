# File generated from our OpenAPI spec by Scalar. See README.md for details.


from ..._models import BaseModel

__all__ = ["AccuracyCitationAnalysisQuery"]


class AccuracyCitationAnalysisQuery(BaseModel):

    category_id: str

    clean_href: str

    start_date: str

    end_date: str
