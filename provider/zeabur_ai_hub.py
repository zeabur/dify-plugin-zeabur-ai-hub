from dify_plugin import ModelProvider


class ZeaburAIHubProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        """
        Validate provider credentials.

        For customizable-model providers, validation happens at the model level,
        so this method can be a no-op.
        """
        pass
