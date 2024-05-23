"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import Optional


class ParcelInsuranceProvider(str, Enum):
    r"""To have insurance cover provided by a carrier directly instead of Shippo's provider (XCover), set provider to `FEDEX`, `UPS`, or `ONTRAC`."""
    FEDEX = 'FEDEX'
    UPS = 'UPS'
    ONTRAC = 'ONTRAC'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ParcelInsurance:
    r"""To add insurace to your parcel, specify `amount`, `content` and `currency`. <br><br>If you do not want to add insurance to you parcel, do not set these parameters."""
    amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""Declared value of the goods you want to insure."""
    content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})
    r"""Description of parcel content."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Currency for the amount value. Currently only USD is supported for FedEx and UPS."""
    provider: Optional[ParcelInsuranceProvider] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider'), 'exclude': lambda f: f is None }})
    r"""To have insurance cover provided by a carrier directly instead of Shippo's provider (XCover), set provider to `FEDEX`, `UPS`, or `ONTRAC`."""
    

