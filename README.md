# Dify Plugin - Gemini

forked from [Official Plugin](https://github.com/langgenius/dify-official-plugins/tree/main/models/gemini)

## Changes

- Add `base_url` parameter.
- Add `Enable file upload` options. (Disable to use `Files API`)
- Modify model parameters.
  - Temperature range: `0.0` - `2.0`
  - Add `response_format` parameter.
  - Add `safety_settings` parameter.
  - Add `thinking_budget` parameter.
  - Add `code_execution` parameter.
- supports `FinishReason.SAFETY`.
- Remove deprecated models.

---

## Other plugins

For more Dify plugins, visit: [https://github.com/blue-pen5805/dify-plugins](https://github.com/blue-pen5805/dify-plugins)
