# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse", "AccuracyCitationClaim", "AccuracyCitationEvidence"]


class AccuracyCitationEvidence(BaseModel):

    kbName: Optional[str] = None

    kbPath: Optional[str] = None

    kbSnippet: Optional[str] = None

class AccuracyCitationClaim(BaseModel):

    claimId: str

    claim: str

    attributeId: str

    attribute: str

    neutralThemeId: str

    neutralTheme: str

    snippet: str

    polarity: Optional[Literal["positive", "negative"]] = None

    kbPath: Optional[str] = None

    kbSnippet: Optional[str] = None

    reasoning: Optional[str] = None

    evidence: Optional[List[AccuracyCitationEvidence]] = None



class AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse(BaseModel):

    href: str

    domain: str

    page_title: str = FieldInfo(alias="pageTitle")

    markdown_content: str = FieldInfo(alias="markdownContent")

    claims: Optional[List[AccuracyCitationClaim]] = None
