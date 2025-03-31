"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CarrierAccountServiceLevelTypedDict(TypedDict):
    r"""Contains details regarding the service level for the carrier account."""

    name: NotRequired[str]
    r"""Service level name, e.g. `Priority Mail` or `FedEx Ground®`.
    A service level commonly defines the transit time of a Shipment (e.g., Express vs. Standard), along with other properties.
    These names vary depending on the provider.<br>
    See <a href=\"#tag/Service-Levels\">Service Levels</a>.
    """
    token: NotRequired[str]
    r"""Service level token, e.g. `usps_priority` or `fedex_ground`.<br>
    See <a href=\"#tag/Service-Levels\">Service Levels</a>.
    """
    supports_return_labels: NotRequired[bool]
    r"""Whether or not the service level supports return labels."""


class CarrierAccountServiceLevel(BaseModel):
    r"""Contains details regarding the service level for the carrier account."""

    name: Optional[str] = None
    r"""Service level name, e.g. `Priority Mail` or `FedEx Ground®`.
    A service level commonly defines the transit time of a Shipment (e.g., Express vs. Standard), along with other properties.
    These names vary depending on the provider.<br>
    See <a href=\"#tag/Service-Levels\">Service Levels</a>.
    """

    token: Optional[str] = None
    r"""Service level token, e.g. `usps_priority` or `fedex_ground`.<br>
    See <a href=\"#tag/Service-Levels\">Service Levels</a>.
    """

    supports_return_labels: Optional[bool] = None
    r"""Whether or not the service level supports return labels."""
