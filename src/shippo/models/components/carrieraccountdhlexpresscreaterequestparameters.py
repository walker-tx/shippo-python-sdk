"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing_extensions import TypedDict


class CarrierAccountDHLExpressCreateRequestParametersTypedDict(TypedDict):
    user_accepted_terms_and_conditions: bool
    r"""Whether or not the user agrees to the DHL Express Terms and Conditions. If passed in as false, request will fail with error 400"""


class CarrierAccountDHLExpressCreateRequestParameters(BaseModel):
    user_accepted_terms_and_conditions: bool
    r"""Whether or not the user agrees to the DHL Express Terms and Conditions. If passed in as false, request will fail with error 400"""
