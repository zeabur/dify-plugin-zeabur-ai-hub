# Changelog

All notable changes to this project will be documented in this file.

## [0.0.12] - 2026-02-12

### Fixed
- Fix plugin dependency installation failure caused by setuptools package discovery

## [0.0.11] - 2026-02-05

### Added
- Add GPT-5.2, GPT-5.1, GPT-5 Nano models
- Add GLM-4.7, GLM-4.7 Flash models
- Add Kimi 2.5 model
- Add Gemini 3 Pro Image Preview, Gemini 2.5 Flash Image models

### Removed
- Remove deepseek-v3.2-exp (not available on Zeabur AI Hub)

## [0.0.10] - 2026-02-01

### Added
- Enable function calling / tool use support for predefined models
- Add model credential form schemas for customizable models (function calling, vision, context size, max tokens)

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
