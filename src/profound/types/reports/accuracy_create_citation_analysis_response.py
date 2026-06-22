# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateCitationAnalysisResponse", "Claim"]


class Claim(BaseModel):
    """A single inaccurate claim mapped to a cluster, surfaced on a cited page.

    ``attribute`` carries the cluster's canonical claim so the drawer can group
    claims the same way it groups sentiment attributes.
    """

    attribute: str

    attribute_id: str = FieldInfo(alias="attributeId")

    claim: str

    claim_id: str = FieldInfo(alias="claimId")

    neutral_theme: str = FieldInfo(alias="neutralTheme")

    neutral_theme_id: str = FieldInfo(alias="neutralThemeId")

    snippet: str

    kb_path: Optional[str] = FieldInfo(alias="kbPath", default=None)

    kb_snippet: Optional[str] = FieldInfo(alias="kbSnippet", default=None)

    polarity: Optional[Literal["positive", "negative"]] = None


class AccuracyCreateCitationAnalysisResponse(BaseModel):
    domain: str

    href: str

    markdown_content: str = FieldInfo(alias="markdownContent")

    page_title: str = FieldInfo(alias="pageTitle")

    claims: Optional[List[Claim]] = None
