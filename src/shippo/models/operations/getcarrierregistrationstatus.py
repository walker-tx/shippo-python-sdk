"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from shippo.types import BaseModel
from shippo.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetCarrierRegistrationStatusGlobalsTypedDict(TypedDict):
    shippo_api_version: NotRequired[str]
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


class GetCarrierRegistrationStatusGlobals(BaseModel):
    shippo_api_version: Annotated[
        Optional[str],
        pydantic.Field(alias="SHIPPO-API-VERSION"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


class Carrier(str, Enum):
    r"""filter by specific carrier"""

    UPS = "ups"
    USPS = "usps"
    CANADA_POST = "canada_post"


class GetCarrierRegistrationStatusRequestTypedDict(TypedDict):
    carrier: Carrier
    r"""filter by specific carrier"""


class GetCarrierRegistrationStatusRequest(BaseModel):
    carrier: Annotated[
        Carrier, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""filter by specific carrier"""
