# Dify Plugin - Gemini

forked from [Official Plugin](https://github.com/langgenius/dify-official-plugins/tree/main/models/gemini).

## Changes

Based on version 0.2.1 of the official plugin.

- Fix `Search Sources` not working.
- Add `base_url` parameter.
- Add `Enable file upload` options. (Disable to use `Files API`)
- Modify model parameters.
  - Add `response_format` parameter.
  - Add `safety_settings` parameter.
  - Add `thinking_budget` parameter.
  - Add `code_execution` parameter.
  - Add `include_search_sources` parameter.
- Supports `FinishReason.SAFETY`.
- Remove deprecated models.

---

## Other plugins

For more Dify plugins, visit: [https://github.com/blue-pen5805/dify-plugins](https://github.com/blue-pen5805/dify-plugins)
