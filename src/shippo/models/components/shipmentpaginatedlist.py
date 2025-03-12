"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .shipment import Shipment, ShipmentTypedDict
from shippo.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ShipmentPaginatedListTypedDict(TypedDict):
    next: NotRequired[str]
    previous: NotRequired[str]
    results: NotRequired[List[ShipmentTypedDict]]


class ShipmentPaginatedList(BaseModel):
    next: Optional[str] = None

    previous: Optional[str] = None

    results: Optional[List[Shipment]] = None
