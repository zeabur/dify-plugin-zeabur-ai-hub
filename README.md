# Zeabur AI Hub Plugin for Dify

Access Claude, Gemini, GPT, DeepSeek and more AI models via [Zeabur AI Hub](https://zeabur.com/ai-hub).

## Features

- Unified API access to multiple AI models
- OpenAI-compatible API format
- Multiple region endpoints (Tokyo, San Francisco)
- 22 pre-configured models ready to use

## Supported Models

| Provider | Models |
|----------|--------|
| Claude | Sonnet 4.5, Haiku 4.5 |
| Gemini | 3 Pro/Flash Preview, 2.5 Pro/Flash/Flash Lite |
| GPT | 5, 5 Mini, 4.1, 4.1 Mini, 4o, 4o Mini, OSS 120B |
| Grok | 4 Fast (Non-Reasoning) |
| DeepSeek | V3.2, V3.2 Exp |
| GLM | 4.6 |
| Kimi | K2 Thinking |
| Llama | 3.3 70B |
| Qwen | 3 32B, 3 Next 80B |

See full model list and pricing at [zeabur.com/models](https://zeabur.com/models)

## Installation

### From Dify Marketplace

Search for **"Zeabur AI Hub"** in Dify Marketplace.

### From GitHub

1. In Dify, go to **Plugins** > **Install from GitHub**
2. Enter: `zeabur/dify-plugin-zeabur-ai-hub`
3. Select the latest version and install

### From Release

1. Download `.difypkg` from [Releases](https://github.com/zeabur/dify-plugin-zeabur-ai-hub/releases)
2. In Dify, go to **Plugins** > **Install from Local File**
3. Upload the downloaded `.difypkg` file

## Configuration

1. Get your API Key from [Zeabur AI Hub](https://zeabur.com/ai-hub)
2. In Dify, go to **Settings** > **Model Provider**
3. Find **Zeabur AI Hub** and click **Setup**
4. Enter:
   - **API Key**: Your Zeabur AI Hub API key
   - **Region**: Select Tokyo (hnd1) or San Francisco (sfo1)
5. Click **Save**

## Links

- [Zeabur AI Hub](https://zeabur.com/ai-hub)
- [Model Pricing](https://zeabur.com/models)
- [Zeabur Documentation](https://zeabur.com/docs)

## Support

- GitHub Issues: https://github.com/zeabur/dify-plugin-zeabur-ai-hub/issues
- Zeabur Discord: https://zeabur.com/discord
- Email: support@zeabur.com

## Repository

https://github.com/zeabur/dify-plugin-zeabur-ai-hub

## Privacy Policy

This plugin connects to Zeabur AI Hub API to provide AI model access.

- **Data Collected**: API requests are sent to Zeabur AI Hub servers
- **Data Storage**: No user data is stored by this plugin
- **Third-party Services**: Requests are processed by Zeabur AI Hub and underlying model providers

For more details, see [Zeabur Privacy Policy](https://zeabur.com/privacy) and [Zeabur Terms of Service](https://zeabur.com/terms).

## Author

**Zeabur** - https://zeabur.com

## License

MIT
