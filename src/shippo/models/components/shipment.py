"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .customsdeclaration import CustomsDeclaration, CustomsDeclarationTypedDict
from .parcel_valid import ParcelValid, ParcelValidTypedDict
from .rate import Rate, RateTypedDict
from .responsemessage import ResponseMessage, ResponseMessageTypedDict
from .shipmentextra import ShipmentExtra, ShipmentExtraTypedDict
from datetime import datetime
from enum import Enum
from shippo.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ShipmentStatus(str, Enum):
    r"""`Waiting` shipments have been successfully submitted but not yet been processed.
    `Queued` shipments are currently being processed.
    `Success` shipments have been processed successfully, meaning that rate generation has concluded.
    `Error` does not occur currently and is reserved for future use.
    """

    ERROR = "ERROR"
    QUEUED = "QUEUED"
    SUCCESS = "SUCCESS"
    WAITING = "WAITING"


class ShipmentTypedDict(TypedDict):
    r"""Shipment represents the parcel as retrieved from the database"""

    metadata: str
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""
    address_from: AddressTypedDict
    r"""<a href=\"#tag/Addresses\">Address</a> object of the sender / seller. Will be returned expanded by default."""
    address_to: AddressTypedDict
    r"""<a href=\"#tag/Addresses\">Address</a> object of the recipient / buyer. Will be returned expanded by default."""
    carrier_accounts: List[str]
    r"""An array of object_ids of the carrier account objects to be used for getting shipping rates for this shipment.
    If no carrier account object_ids are set in this field, Shippo will attempt to generate rates using all the
    carrier accounts that have the `active` field set.
    """
    messages: List[ResponseMessageTypedDict]
    object_created: datetime
    r"""Date and time of Shipment creation."""
    object_id: str
    r"""Unique identifier of the given Shipment object."""
    object_owner: str
    r"""Username of the user who created the Shipment object."""
    object_updated: datetime
    r"""Date and time of last Shipment update."""
    parcels: List[ParcelValidTypedDict]
    r"""List of Parcel objects to be shipped."""
    rates: List[RateTypedDict]
    r"""An array with all available rates. If <code>async</code> has been set to <code>false</code> in the request,
    this will be populated with all available rates in the response. Otherwise rates will be created
    asynchronously and this array will initially be empty.
    """
    status: ShipmentStatus
    r"""`Waiting` shipments have been successfully submitted but not yet been processed.
    `Queued` shipments are currently being processed.
    `Success` shipments have been processed successfully, meaning that rate generation has concluded.
    `Error` does not occur currently and is reserved for future use.
    """
    extra: NotRequired[ShipmentExtraTypedDict]
    r"""An object holding optional extra services to be requested."""
    shipment_date: NotRequired[str]
    r"""Date the shipment will be tendered to the carrier. Must be in the format `2014-01-18T00:35:03.463Z`.
    Defaults to current date and time if no value is provided. Please note that some carriers require this value to
    be in the future, on a working day, or similar.
    """
    address_return: NotRequired[AddressTypedDict]
    r"""ID of the Address object where the shipment will be sent back to if it is not delivered
    (Only available for UPS, USPS, and Fedex shipments). <br/>
    If this field is not set, your shipments will be returned to the address_from.
    """
    customs_declaration: NotRequired[CustomsDeclarationTypedDict]
    test: NotRequired[bool]
    r"""Indicates whether the object has been created in test mode."""


class Shipment(BaseModel):
    r"""Shipment represents the parcel as retrieved from the database"""

    metadata: str
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""

    address_from: Address
    r"""<a href=\"#tag/Addresses\">Address</a> object of the sender / seller. Will be returned expanded by default."""

    address_to: Address
    r"""<a href=\"#tag/Addresses\">Address</a> object of the recipient / buyer. Will be returned expanded by default."""

    carrier_accounts: List[str]
    r"""An array of object_ids of the carrier account objects to be used for getting shipping rates for this shipment.
    If no carrier account object_ids are set in this field, Shippo will attempt to generate rates using all the
    carrier accounts that have the `active` field set.
    """

    messages: List[ResponseMessage]

    object_created: datetime
    r"""Date and time of Shipment creation."""

    object_id: str
    r"""Unique identifier of the given Shipment object."""

    object_owner: str
    r"""Username of the user who created the Shipment object."""

    object_updated: datetime
    r"""Date and time of last Shipment update."""

    parcels: List[ParcelValid]
    r"""List of Parcel objects to be shipped."""

    rates: List[Rate]
    r"""An array with all available rates. If <code>async</code> has been set to <code>false</code> in the request,
    this will be populated with all available rates in the response. Otherwise rates will be created
    asynchronously and this array will initially be empty.
    """

    status: ShipmentStatus
    r"""`Waiting` shipments have been successfully submitted but not yet been processed.
    `Queued` shipments are currently being processed.
    `Success` shipments have been processed successfully, meaning that rate generation has concluded.
    `Error` does not occur currently and is reserved for future use.
    """

    extra: Optional[ShipmentExtra] = None
    r"""An object holding optional extra services to be requested."""

    shipment_date: Optional[str] = None
    r"""Date the shipment will be tendered to the carrier. Must be in the format `2014-01-18T00:35:03.463Z`.
    Defaults to current date and time if no value is provided. Please note that some carriers require this value to
    be in the future, on a working day, or similar.
    """

    address_return: Optional[Address] = None
    r"""ID of the Address object where the shipment will be sent back to if it is not delivered
    (Only available for UPS, USPS, and Fedex shipments). <br/>
    If this field is not set, your shipments will be returned to the address_from.
    """

    customs_declaration: Optional[CustomsDeclaration] = None

    test: Optional[bool] = None
    r"""Indicates whether the object has been created in test mode."""
