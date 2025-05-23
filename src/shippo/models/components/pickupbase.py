"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .location import Location, LocationTypedDict
from datetime import datetime
from shippo.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PickupBaseTypedDict(TypedDict):
    carrier_account: str
    r"""The object ID of your USPS or DHL Express carrier account.
    You can retrieve this from your Rate requests or our <a href=\"#tag/Carrier-Accounts/\">Carrier Accounts</a> endpoint.
    """
    location: LocationTypedDict
    r"""Location where the parcel(s) will be picked up."""
    requested_end_time: datetime
    r"""The latest that you requested your parcels to be available for pickup.
    Expressed in the timezone specified in the response.
    """
    requested_start_time: datetime
    r"""The earliest that you requested your parcels to be ready for pickup.
    Expressed in the timezone specified in the response.
    """
    transactions: List[str]
    r"""The transaction(s) object ID(s) for the parcel(s) that need to be picked up."""
    metadata: NotRequired[str]
    r"""A string of up to 100 characters that can be filled with any additional information you
    want to attach to the object.
    """


class PickupBase(BaseModel):
    carrier_account: str
    r"""The object ID of your USPS or DHL Express carrier account.
    You can retrieve this from your Rate requests or our <a href=\"#tag/Carrier-Accounts/\">Carrier Accounts</a> endpoint.
    """

    location: Location
    r"""Location where the parcel(s) will be picked up."""

    requested_end_time: datetime
    r"""The latest that you requested your parcels to be available for pickup.
    Expressed in the timezone specified in the response.
    """

    requested_start_time: datetime
    r"""The earliest that you requested your parcels to be ready for pickup.
    Expressed in the timezone specified in the response.
    """

    transactions: List[str]
    r"""The transaction(s) object ID(s) for the parcel(s) that need to be picked up."""

    metadata: Optional[str] = None
    r"""A string of up to 100 characters that can be filled with any additional information you
    want to attach to the object.
    """
