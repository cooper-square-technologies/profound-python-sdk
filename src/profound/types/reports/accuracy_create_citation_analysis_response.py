# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateCitationAnalysisResponse", "Claim", "ClaimEvidence"]


class ClaimEvidence(BaseModel):
    """A single knowledge-base ground-truth snippet that refutes a claim's cluster.

    ``kb_name`` is the official knowledge base name; ``kb_path`` is the document
    path within that knowledge base. ``kb_name`` is populated by the external API
    layer (which can reach the knowledge-base service) and defaults to ``""``
    elsewhere.
    """

    kb_name: Optional[str] = FieldInfo(alias="kbName", default=None)

    kb_path: Optional[str] = FieldInfo(alias="kbPath", default=None)

    kb_snippet: Optional[str] = FieldInfo(alias="kbSnippet", default=None)


class Claim(BaseModel):
    """A single inaccurate claim mapped to a cluster, surfaced on a cited page.

    ``attribute`` carries the cluster's canonical claim so the drawer can group
    claims the same way it groups sentiment attributes.

    ``reasoning`` and ``evidence`` mirror the cluster's FactCheck verdict: the
    "why it's inaccurate" explanation plus the refuting knowledge-base snippets
    surfaced in the Claim Analysis drawer. ``kb_path``/``kb_snippet`` are retained
    as the cluster's single representative snippet for backward compatibility.
    """

    attribute: str

    attribute_id: str = FieldInfo(alias="attributeId")

    claim: str

    claim_id: str = FieldInfo(alias="claimId")

    neutral_theme: str = FieldInfo(alias="neutralTheme")

    neutral_theme_id: str = FieldInfo(alias="neutralThemeId")

    snippet: str

    evidence: Optional[List[ClaimEvidence]] = None

    kb_path: Optional[str] = FieldInfo(alias="kbPath", default=None)

    kb_snippet: Optional[str] = FieldInfo(alias="kbSnippet", default=None)

    polarity: Optional[Literal["positive", "negative"]] = None

    reasoning: Optional[str] = None


class AccuracyCreateCitationAnalysisResponse(BaseModel):
    domain: str

    href: str

    markdown_content: str = FieldInfo(alias="markdownContent")

    page_title: str = FieldInfo(alias="pageTitle")

    claims: Optional[List[Claim]] = None
