"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .servicelevelwithparent import (
    ServiceLevelWithParent,
    ServiceLevelWithParentTypedDict,
)
from .trackingstatus import TrackingStatus, TrackingStatusTypedDict
from .trackingstatuslocationbase import (
    TrackingStatusLocationBase,
    TrackingStatusLocationBaseTypedDict,
)
from datetime import datetime
from shippo.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TrackTypedDict(TypedDict):
    carrier: str
    r"""Name of the carrier of the shipment to track. See <a href=\"#tag/Carriers\">Carriers</a>."""
    messages: List[str]
    tracking_history: List[TrackingStatusTypedDict]
    r"""A list of tracking events, following the same structure as <code>tracking_status</code>.
    It contains a full history of all tracking statuses, starting with the earlier tracking event first.
    """
    tracking_number: str
    r"""Tracking number to track."""
    address_from: NotRequired[TrackingStatusLocationBaseTypedDict]
    r"""The sender address with city, state, zip and country information."""
    address_to: NotRequired[TrackingStatusLocationBaseTypedDict]
    r"""The recipient address with city, state, zip and country information."""
    eta: NotRequired[datetime]
    r"""The estimated time of arrival according to the carrier, this might be updated by carriers during the life of the shipment."""
    metadata: NotRequired[str]
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""
    original_eta: NotRequired[datetime]
    r"""The estimated time of arrival according to the carrier at the time the shipment first entered the system."""
    servicelevel: NotRequired[ServiceLevelWithParentTypedDict]
    tracking_status: NotRequired[TrackingStatusTypedDict]
    r"""The latest tracking information of this shipment."""
    transaction: NotRequired[str]
    r"""The <code>object_id</code> of the transaction associated with this tracking object.
    This field is visible only to the object owner of the transaction.
    """


class Track(BaseModel):
    carrier: str
    r"""Name of the carrier of the shipment to track. See <a href=\"#tag/Carriers\">Carriers</a>."""

    messages: List[str]

    tracking_history: List[TrackingStatus]
    r"""A list of tracking events, following the same structure as <code>tracking_status</code>.
    It contains a full history of all tracking statuses, starting with the earlier tracking event first.
    """

    tracking_number: str
    r"""Tracking number to track."""

    address_from: Optional[TrackingStatusLocationBase] = None
    r"""The sender address with city, state, zip and country information."""

    address_to: Optional[TrackingStatusLocationBase] = None
    r"""The recipient address with city, state, zip and country information."""

    eta: Optional[datetime] = None
    r"""The estimated time of arrival according to the carrier, this might be updated by carriers during the life of the shipment."""

    metadata: Optional[str] = None
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""

    original_eta: Optional[datetime] = None
    r"""The estimated time of arrival according to the carrier at the time the shipment first entered the system."""

    servicelevel: Optional[ServiceLevelWithParent] = None

    tracking_status: Optional[TrackingStatus] = None
    r"""The latest tracking information of this shipment."""

    transaction: Optional[str] = None
    r"""The <code>object_id</code> of the transaction associated with this tracking object.
    This field is visible only to the object owner of the transaction.
    """
