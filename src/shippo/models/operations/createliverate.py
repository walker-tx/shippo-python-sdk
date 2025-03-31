"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from shippo.types import BaseModel
from shippo.utils import FieldMetadata, HeaderMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateLiveRateGlobalsTypedDict(TypedDict):
    shippo_api_version: NotRequired[str]
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


class CreateLiveRateGlobals(BaseModel):
    shippo_api_version: Annotated[
        Optional[str],
        pydantic.Field(alias="SHIPPO-API-VERSION"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""
