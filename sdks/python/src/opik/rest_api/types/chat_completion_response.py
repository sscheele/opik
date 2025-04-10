# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .chat_completion_choice import ChatCompletionChoice
from .usage import Usage
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ChatCompletionResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    created: typing.Optional[int] = None
    model: typing.Optional[str] = None
    choices: typing.Optional[typing.List[ChatCompletionChoice]] = None
    usage: typing.Optional[Usage] = None
    system_fingerprint: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
