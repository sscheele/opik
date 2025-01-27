# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .llm_as_judge_code_public import LlmAsJudgeCodePublic


class Base(UniversalBaseModel):
    id: typing.Optional[str] = None
    project_id: typing.Optional[str] = None
    name: str
    sampling_rate: typing.Optional[float] = None
    created_at: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    last_updated_at: typing.Optional[dt.datetime] = None
    last_updated_by: typing.Optional[str] = None
    action: typing.Optional[typing.Literal["evaluator"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AutomationRuleEvaluatorPublic_LlmAsJudge(Base):
    type: typing.Literal["llm_as_judge"] = "llm_as_judge"
    code: typing.Optional[LlmAsJudgeCodePublic] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AutomationRuleEvaluatorPublic = AutomationRuleEvaluatorPublic_LlmAsJudge
