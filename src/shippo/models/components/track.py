"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .servicelevelwithparent import ServiceLevelWithParent
from .trackingstatus import TrackingStatus
from .trackingstatuslocationbase import TrackingStatusLocationBase
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from shippo import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Track:
    carrier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier') }})
    r"""Name of the carrier of the shipment to track. See <a href=\\"#tag/Carriers\\">Carriers</a>."""
    messages: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('messages') }})
    tracking_history: List[TrackingStatus] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking_history') }})
    r"""A list of tracking events, following the same structure as <code>tracking_status</code>.
    It contains a full history of all tracking statuses, starting with the earlier tracking event first.
    """
    tracking_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking_number') }})
    r"""Tracking number to track."""
    address_from: Optional[TrackingStatusLocationBase] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_from'), 'exclude': lambda f: f is None }})
    r"""The sender address with city, state, zip and country information."""
    address_to: Optional[TrackingStatusLocationBase] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_to'), 'exclude': lambda f: f is None }})
    r"""The recipient address with city, state, zip and country information."""
    eta: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eta'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The estimated time of arrival according to the carrier, this might be updated by carriers during the life of the shipment."""
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""
    original_eta: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('original_eta'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The estimated time of arrival according to the carrier at the time the shipment first entered the system."""
    servicelevel: Optional[ServiceLevelWithParent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servicelevel'), 'exclude': lambda f: f is None }})
    tracking_status: Optional[TrackingStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking_status'), 'exclude': lambda f: f is None }})
    r"""The latest tracking information of this shipment."""
    transaction: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction'), 'exclude': lambda f: f is None }})
    r"""The <code>object_id</code> of the transaction associated with this tracking object.
    This field is visible only to the object owner of the transaction.
    """
    

