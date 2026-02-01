from typing import Optional
from collections.abc import Generator

from dify_plugin.entities.model import AIModelEntity, FetchFrom, ModelFeature, ModelType
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

    def get_customizable_model_schema(self, model: str, credentials: dict) -> Optional[AIModelEntity]:
        """
        Get customizable model schema for user-added models.

        This method defines the features and parameters for custom models based on
        the credential values provided by the user.
        """
        self._add_custom_parameters(credentials)

        # Get base entity from parent class
        entity = super().get_customizable_model_schema(model, credentials)
        if entity is None:
            return None

        # Initialize features list if not present
        features = list(entity.features) if entity.features else []

        # Add function calling features based on credentials
        function_calling_type = credentials.get("function_calling_type", "tool_call")
        if function_calling_type in ("tool_call", "function_call"):
            if ModelFeature.TOOL_CALL not in features:
                features.append(ModelFeature.TOOL_CALL)

            # Add stream tool call if supported
            stream_function_calling = credentials.get("stream_function_calling", "supported")
            if stream_function_calling == "supported":
                if ModelFeature.STREAM_TOOL_CALL not in features:
                    features.append(ModelFeature.STREAM_TOOL_CALL)

        # Add vision support if enabled
        vision_support = credentials.get("vision_support", "not_supported")
        if vision_support == "supported":
            if ModelFeature.VISION not in features:
                features.append(ModelFeature.VISION)

        # Always add agent thought support
        if ModelFeature.AGENT_THOUGHT not in features:
            features.append(ModelFeature.AGENT_THOUGHT)

        # Create updated entity with features
        return AIModelEntity(
            model=entity.model,
            label=entity.label,
            model_type=ModelType.LLM,
            features=features,
            fetch_from=FetchFrom.CUSTOMIZABLE_MODEL,
            model_properties=entity.model_properties,
            parameter_rules=entity.parameter_rules,
        )

    @staticmethod
    def _add_custom_parameters(credentials: dict) -> None:
        credentials["mode"] = "chat"
        # Set function calling type to tool_call if not already specified
        # This enables function calling / tool use for the model
        if "function_calling_type" not in credentials:
            credentials["function_calling_type"] = "tool_call"
        # Enable streaming function calling if not already specified
        if "stream_function_calling" not in credentials:
            credentials["stream_function_calling"] = "supported"
