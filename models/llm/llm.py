from typing import Optional
from collections.abc import Generator

from dify_plugin.entities.model import AIModelEntity
from dify_plugin.entities.model.llm import LLMResult, LLMResultChunk
from dify_plugin.entities.model.message import PromptMessage, PromptMessageTool
from dify_plugin.interfaces.model.openai_compatible.llm import OAICompatLargeLanguageModel


class ZeaburLargeLanguageModel(OAICompatLargeLanguageModel):
    """
    Zeabur AI Hub LLM implementation.

    Since Zeabur AI Hub is built on LiteLLM and uses the OpenAI-compatible API format,
    we extend the OAICompatLargeLanguageModel base class and add custom parameters.
    """

    def _invoke(
        self,
        model: str,
        credentials: dict,
        prompt_messages: list[PromptMessage],
        model_parameters: dict,
        tools: Optional[list[PromptMessageTool]] = None,
        stop: Optional[list[str]] = None,
        stream: bool = True,
        user: Optional[str] = None,
    ) -> Generator[LLMResultChunk, None, None] | LLMResult:
        self._add_custom_parameters(credentials)
        return super()._invoke(model, credentials, prompt_messages, model_parameters, tools, stop, stream, user)

    def validate_credentials(self, model: str, credentials: dict) -> None:
        self._add_custom_parameters(credentials)
        super().validate_credentials(model, credentials)

    @staticmethod
    def _add_custom_parameters(credentials: dict) -> None:
        credentials["mode"] = "chat"
