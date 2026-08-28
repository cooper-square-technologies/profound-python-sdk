# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateCitationAnalysisResponse", "Claim", "ClaimEvidence"]


class ClaimEvidence(BaseModel):
    kb_name: Optional[str] = FieldInfo(alias="kbName", default=None)

    kb_path: Optional[str] = FieldInfo(alias="kbPath", default=None)

    kb_snippet: Optional[str] = FieldInfo(alias="kbSnippet", default=None)


class Claim(BaseModel):
    claim_id: str = FieldInfo(alias="claimId")

    claim: str

    attribute_id: str = FieldInfo(alias="attributeId")

    attribute: str

    neutral_theme_id: str = FieldInfo(alias="neutralThemeId")

    neutral_theme: str = FieldInfo(alias="neutralTheme")

    snippet: str

    polarity: Optional[Literal["positive", "negative"]] = None

    kb_path: Optional[str] = FieldInfo(alias="kbPath", default=None)

    kb_snippet: Optional[str] = FieldInfo(alias="kbSnippet", default=None)

    reasoning: Optional[str] = None

    evidence: Optional[List[ClaimEvidence]] = None


class AccuracyCreateCitationAnalysisResponse(BaseModel):
    href: str

    domain: str

    page_title: str = FieldInfo(alias="pageTitle")

    markdown_content: str = FieldInfo(alias="markdownContent")

    claims: Optional[List[Claim]] = None
