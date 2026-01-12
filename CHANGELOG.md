# Changelog

All notable changes to this project will be documented in this file.

## [0.0.9] - 2026-01-12

### Added
- Add privacy policy (PRIVACY.md)

## [0.0.8] - 2026-01-09

### Added
- Add missing official API parameters for all models:
  - **Claude**: `top_k`, `thinking_budget_tokens`
  - **GPT (4o, 4.1, 5 series)**: `seed`, `json_schema`, `logprobs`, `top_logprobs`
  - **Gemini**: `top_k`, `presence_penalty`, `seed`, `json_schema`, `reasoning_effort`, `include_reasoning`
  - **DeepSeek**: `logprobs`, `top_logprobs`
  - **Qwen**: `top_k`, `presence_penalty`, `frequency_penalty`, `repetition_penalty`, `response_format`
  - **GLM**: `response_format`
  - **Kimi**: `presence_penalty`, `response_format`
  - **Grok**: `presence_penalty`, `frequency_penalty`
  - **Llama**: `top_k`, `repetition_penalty`, `response_format`

### Changed
- Align model parameters with LiteLLM documentation

## [0.0.7] - 2026-01-08

### Added
- Initial marketplace release
- Support for Claude, Gemini, GPT, DeepSeek, Qwen, GLM, Kimi, Grok, Llama models
