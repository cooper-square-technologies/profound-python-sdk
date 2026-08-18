# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyFactcheckSetupStatusV1FactcheckSetupStatusPostResponse"]


class AccuracyFactcheckSetupStatusV1FactcheckSetupStatusPostResponse(BaseModel):
    active_accuracy_prompt_count: int = FieldInfo(alias="activeAccuracyPromptCount")

    has_verification_data: bool = FieldInfo(alias="hasVerificationData")

    is_setup_complete: bool = FieldInfo(alias="isSetupComplete")

    setup_created_at: Optional[str] = FieldInfo(alias="setupCreatedAt", default=None)

    setup_knowledge_base_id: Optional[str] = FieldInfo(alias="setupKnowledgeBaseId", default=None)
