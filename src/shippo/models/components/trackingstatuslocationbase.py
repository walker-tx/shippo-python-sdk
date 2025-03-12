"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class TrackingStatusLocationBaseTypedDict(TypedDict):
    city: NotRequired[str]
    country: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]


class TrackingStatusLocationBase(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    state: Optional[str] = None

    zip: Optional[str] = None
