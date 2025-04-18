import typing
from enum import Enum
from typing import Optional, Union
from typing_extensions import TypedDict
import pydantic
from pydantic import Field

from google.genai import _common, models, types
from google.genai._api_client import ApiClient
from google.genai._common import get_value_by_path as getv
from google.genai._common import set_value_by_path as setv
from google.genai.types import (
    HttpOptions, HttpOptionsDict,
    ContentUnion, ContentUnionDict,
    SchemaUnion, SchemaUnionDict,
    GenerationConfigRoutingConfig, GenerationConfigRoutingConfigDict,
    SafetySetting, SafetySettingDict,
    ToolListUnion, ToolListUnionDict,
    ToolConfig, ToolConfigDict,
    MediaResolution,
    SpeechConfigUnion, SpeechConfigUnionDict,
    AutomaticFunctionCallingConfig, AutomaticFunctionCallingConfigDict,
    ContentListUnion, ContentListUnionDict,
)

# ThinkingConfig
# https://github.com/googleapis/python-genai/blob/v1.2.0/google/genai/types.py#L1520-L1538
# https://github.com/googleapis/python-genai/blob/v1.11.0/google/genai/types.py#L2069-L2096
class ThinkingConfig(_common.BaseModel):
  """The thinking features configuration."""

  include_thoughts: Optional[bool] = Field(
      default=None,
      description="""Indicates whether to include thoughts in the response. If true, thoughts are returned only if the model supports thought and thoughts are available.
      """,
  )
  thinking_budget: Optional[int] = Field(
      default=None,
      description="""Indicates the thinking budget in tokens.
      """,
  )


class ThinkingConfigDict(TypedDict, total=False):
  """The thinking features configuration."""

  include_thoughts: Optional[bool]
  """Indicates whether to include thoughts in the response. If true, thoughts are returned only if the model supports thought and thoughts are available.
      """

  thinking_budget: Optional[int]
  """Indicates the thinking budget in tokens.
      """

ThinkingConfigOrDict = Union[ThinkingConfig, ThinkingConfigDict]

types.ThinkingConfig = ThinkingConfig
types.ThinkingConfigDict = ThinkingConfigDict
types.ThinkingConfigOrDict = ThinkingConfigOrDict

# GenerateContentConfig
# https://github.com/googleapis/python-genai/blob/v1.2.0/google/genai/types.py#L1776-L2097

class GenerateContentConfig(_common.BaseModel):
  """Optional model configuration parameters.

  For more information, see `Content generation parameters
  <https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters>`_.
  """

  http_options: Optional[HttpOptions] = Field(
      default=None, description="""Used to override HTTP request options."""
  )
  system_instruction: Optional[ContentUnion] = Field(
      default=None,
      description="""Instructions for the model to steer it toward better performance.
      For example, "Answer as concisely as possible" or "Don't use technical
      terms in your response".
      """,
  )
  temperature: Optional[float] = Field(
      default=None,
      description="""Value that controls the degree of randomness in token selection.
      Lower temperatures are good for prompts that require a less open-ended or
      creative response, while higher temperatures can lead to more diverse or
      creative results.
      """,
  )
  top_p: Optional[float] = Field(
      default=None,
      description="""Tokens are selected from the most to least probable until the sum
      of their probabilities equals this value. Use a lower value for less
      random responses and a higher value for more random responses.
      """,
  )
  top_k: Optional[float] = Field(
      default=None,
      description="""For each token selection step, the ``top_k`` tokens with the
      highest probabilities are sampled. Then tokens are further filtered based
      on ``top_p`` with the final token selected using temperature sampling. Use
      a lower number for less random responses and a higher number for more
      random responses.
      """,
  )
  candidate_count: Optional[int] = Field(
      default=None,
      description="""Number of response variations to return.
      """,
  )
  max_output_tokens: Optional[int] = Field(
      default=None,
      description="""Maximum number of tokens that can be generated in the response.
      """,
  )
  stop_sequences: Optional[list[str]] = Field(
      default=None,
      description="""List of strings that tells the model to stop generating text if one
      of the strings is encountered in the response.
      """,
  )
  response_logprobs: Optional[bool] = Field(
      default=None,
      description="""Whether to return the log probabilities of the tokens that were
      chosen by the model at each step.
      """,
  )
  logprobs: Optional[int] = Field(
      default=None,
      description="""Number of top candidate tokens to return the log probabilities for
      at each generation step.
      """,
  )
  presence_penalty: Optional[float] = Field(
      default=None,
      description="""Positive values penalize tokens that already appear in the
      generated text, increasing the probability of generating more diverse
      content.
      """,
  )
  frequency_penalty: Optional[float] = Field(
      default=None,
      description="""Positive values penalize tokens that repeatedly appear in the
      generated text, increasing the probability of generating more diverse
      content.
      """,
  )
  seed: Optional[int] = Field(
      default=None,
      description="""When ``seed`` is fixed to a specific number, the model makes a best
      effort to provide the same response for repeated requests. By default, a
      random number is used.
      """,
  )
  response_mime_type: Optional[str] = Field(
      default=None,
      description="""Output response media type of the generated candidate text.
      """,
  )
  response_schema: Optional[SchemaUnion] = Field(
      default=None,
      description="""Schema that the generated candidate text must adhere to.
      """,
  )
  routing_config: Optional[GenerationConfigRoutingConfig] = Field(
      default=None,
      description="""Configuration for model router requests.
      """,
  )
  safety_settings: Optional[list[SafetySetting]] = Field(
      default=None,
      description="""Safety settings in the request to block unsafe content in the
      response.
      """,
  )
  tools: Optional[ToolListUnion] = Field(
      default=None,
      description="""Code that enables the system to interact with external systems to
      perform an action outside of the knowledge and scope of the model.
      """,
  )
  tool_config: Optional[ToolConfig] = Field(
      default=None,
      description="""Associates model output to a specific function call.
      """,
  )
  labels: Optional[dict[str, str]] = Field(
      default=None,
      description="""Labels with user-defined metadata to break down billed charges.""",
  )
  cached_content: Optional[str] = Field(
      default=None,
      description="""Resource name of a context cache that can be used in subsequent
      requests.
      """,
  )
  response_modalities: Optional[list[str]] = Field(
      default=None,
      description="""The requested modalities of the response. Represents the set of
      modalities that the model can return.
      """,
  )
  media_resolution: Optional[MediaResolution] = Field(
      default=None,
      description="""If specified, the media resolution specified will be used.
    """,
  )
  speech_config: Optional[SpeechConfigUnion] = Field(
      default=None,
      description="""The speech generation configuration.
      """,
  )
  audio_timestamp: Optional[bool] = Field(
      default=None,
      description="""If enabled, audio timestamp will be included in the request to the
       model.
      """,
  )
  automatic_function_calling: Optional[AutomaticFunctionCallingConfig] = Field(
      default=None,
      description="""The configuration for automatic function calling.
      """,
  )
  thinking_config: Optional[ThinkingConfig] = Field(
      default=None,
      description="""The thinking features configuration.
      """,
  )

  @pydantic.field_validator('response_schema', mode='before')
  @classmethod
  def _convert_literal_to_enum(cls, value):
    if typing.get_origin(value) is typing.Literal:
      enum_vals = typing.get_args(value)
      if not all(isinstance(arg, str) for arg in enum_vals):
        # This doesn't stop execution, it tells pydantic to raise a ValidationError
        # when the class is instantiated with an unsupported Literal
        raise ValueError(f'Literal type {value} must be a list of strings.')
      # The title 'PlaceholderLiteralEnum' is removed from the generated Schema
      # before sending the request
      return Enum('PlaceholderLiteralEnum', {s: s for s in enum_vals})
    return value


class GenerateContentConfigDict(TypedDict, total=False):
  """Optional model configuration parameters.

  For more information, see `Content generation parameters
  <https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters>`_.
  """

  http_options: Optional[HttpOptionsDict]
  """Used to override HTTP request options."""

  system_instruction: Optional[ContentUnionDict]
  """Instructions for the model to steer it toward better performance.
      For example, "Answer as concisely as possible" or "Don't use technical
      terms in your response".
      """

  temperature: Optional[float]
  """Value that controls the degree of randomness in token selection.
      Lower temperatures are good for prompts that require a less open-ended or
      creative response, while higher temperatures can lead to more diverse or
      creative results.
      """

  top_p: Optional[float]
  """Tokens are selected from the most to least probable until the sum
      of their probabilities equals this value. Use a lower value for less
      random responses and a higher value for more random responses.
      """

  top_k: Optional[float]
  """For each token selection step, the ``top_k`` tokens with the
      highest probabilities are sampled. Then tokens are further filtered based
      on ``top_p`` with the final token selected using temperature sampling. Use
      a lower number for less random responses and a higher number for more
      random responses.
      """

  candidate_count: Optional[int]
  """Number of response variations to return.
      """

  max_output_tokens: Optional[int]
  """Maximum number of tokens that can be generated in the response.
      """

  stop_sequences: Optional[list[str]]
  """List of strings that tells the model to stop generating text if one
      of the strings is encountered in the response.
      """

  response_logprobs: Optional[bool]
  """Whether to return the log probabilities of the tokens that were
      chosen by the model at each step.
      """

  logprobs: Optional[int]
  """Number of top candidate tokens to return the log probabilities for
      at each generation step.
      """

  presence_penalty: Optional[float]
  """Positive values penalize tokens that already appear in the
      generated text, increasing the probability of generating more diverse
      content.
      """

  frequency_penalty: Optional[float]
  """Positive values penalize tokens that repeatedly appear in the
      generated text, increasing the probability of generating more diverse
      content.
      """

  seed: Optional[int]
  """When ``seed`` is fixed to a specific number, the model makes a best
      effort to provide the same response for repeated requests. By default, a
      random number is used.
      """

  response_mime_type: Optional[str]
  """Output response media type of the generated candidate text.
      """

  response_schema: Optional[SchemaUnionDict]
  """Schema that the generated candidate text must adhere to.
      """

  routing_config: Optional[GenerationConfigRoutingConfigDict]
  """Configuration for model router requests.
      """

  safety_settings: Optional[list[SafetySettingDict]]
  """Safety settings in the request to block unsafe content in the
      response.
      """

  tools: Optional[ToolListUnionDict]
  """Code that enables the system to interact with external systems to
      perform an action outside of the knowledge and scope of the model.
      """

  tool_config: Optional[ToolConfigDict]
  """Associates model output to a specific function call.
      """

  labels: Optional[dict[str, str]]
  """Labels with user-defined metadata to break down billed charges."""

  cached_content: Optional[str]
  """Resource name of a context cache that can be used in subsequent
      requests.
      """

  response_modalities: Optional[list[str]]
  """The requested modalities of the response. Represents the set of
      modalities that the model can return.
      """

  media_resolution: Optional[MediaResolution]
  """If specified, the media resolution specified will be used.
    """

  speech_config: Optional[SpeechConfigUnionDict]
  """The speech generation configuration.
      """

  audio_timestamp: Optional[bool]
  """If enabled, audio timestamp will be included in the request to the
       model.
      """

  automatic_function_calling: Optional[AutomaticFunctionCallingConfigDict]
  """The configuration for automatic function calling.
      """

  thinking_config: Optional[ThinkingConfigDict]
  """The thinking features configuration.
      """


GenerateContentConfigOrDict = Union[
    GenerateContentConfig, GenerateContentConfigDict
]

types.GenerateContentConfig = GenerateContentConfig
types.GenerateContentConfigDict = GenerateContentConfigDict
types.GenerateContentConfigOrDict = GenerateContentConfigOrDict

# GenerateContentParameters
# https://github.com/googleapis/python-genai/blob/v1.2.0/google/genai/types.py#L2106C1-L2144C2

class _GenerateContentParameters(_common.BaseModel):
  """Config for models.generate_content parameters."""

  model: Optional[str] = Field(
      default=None,
      description="""ID of the model to use. For a list of models, see `Google models
    <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models>`_.""",
  )
  contents: Optional[ContentListUnion] = Field(
      default=None,
      description="""Content of the request.
      """,
  )
  config: Optional[GenerateContentConfig] = Field(
      default=None,
      description="""Configuration that contains optional model parameters.
      """,
  )


class _GenerateContentParametersDict(TypedDict, total=False):
  """Config for models.generate_content parameters."""

  model: Optional[str]
  """ID of the model to use. For a list of models, see `Google models
    <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models>`_."""

  contents: Optional[ContentListUnionDict]
  """Content of the request.
      """

  config: Optional[GenerateContentConfigDict]
  """Configuration that contains optional model parameters.
      """


_GenerateContentParametersOrDict = Union[
    _GenerateContentParameters, _GenerateContentParametersDict
]

types._GenerateContentParameters = _GenerateContentParameters
types._GenerateContentParametersDict = _GenerateContentParametersDict
types._GenerateContentParametersOrDict = _GenerateContentParametersOrDict

# _ThinkingConfig_to_mldev
# https://github.com/googleapis/python-genai/blob/v1.2.0/google/genai/models.py#L768-L779

def _ThinkingConfig_to_mldev(
    api_client: ApiClient,
    from_object: Union[dict, object],
    parent_object: dict = None,
) -> dict:
  to_object = {}
  if getv(from_object, ['include_thoughts']) is not None:
    setv(
        to_object, ['includeThoughts'], getv(from_object, ['include_thoughts'])
    )

  if getv(from_object, ['thinking_budget']) is not None:
    setv(to_object, ['thinkingBudget'], getv(from_object, ['thinking_budget']))

  return to_object

models._ThinkingConfig_to_mldev = _ThinkingConfig_to_mldev
