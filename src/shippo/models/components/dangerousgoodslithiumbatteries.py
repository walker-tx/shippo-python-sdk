"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DangerousGoodsLithiumBatteriesTypedDict(TypedDict):
    r"""Container for specifying the presence of lithium batteries."""

    contains: NotRequired[bool]
    r"""Indicates if the shipment contains lithium batteries."""


class DangerousGoodsLithiumBatteries(BaseModel):
    r"""Container for specifying the presence of lithium batteries."""

    contains: Optional[bool] = None
    r"""Indicates if the shipment contains lithium batteries."""
