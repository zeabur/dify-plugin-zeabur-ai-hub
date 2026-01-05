from collections.abc import Mapping

from dify_plugin.interfaces.model.openai_compatible.llm import OAICompatLargeLanguageModel


class ZeaburLargeLanguageModel(OAICompatLargeLanguageModel):
    """
    Zeabur AI Hub LLM implementation.

    Since Zeabur AI Hub is built on LiteLLM and uses the OpenAI-compatible API format,
    we can simply extend the OAICompatLargeLanguageModel base class.
    """

    def _get_api_url(self, credentials: Mapping) -> str:
        """
        Get the API URL based on the selected region endpoint.

        Available endpoints:
        - hnd1: Tokyo, Japan (https://hnd1.aihub.zeabur.ai/v1)
        - sfo1: San Francisco, USA (https://sfo1.aihub.zeabur.ai/v1)
        """
        endpoint = credentials.get("endpoint", "hnd1")
        return f"https://{endpoint}.aihub.zeabur.ai/v1"

    def _get_api_key(self, credentials: Mapping) -> str:
        """Get the API key from credentials."""
        return credentials.get("api_key", "")
