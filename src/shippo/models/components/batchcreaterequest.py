"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .batchshipmentcreaterequest import (
    BatchShipmentCreateRequest,
    BatchShipmentCreateRequestTypedDict,
)
from .labelfiletypeenum import LabelFileTypeEnum
from shippo.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class BatchCreateRequestTypedDict(TypedDict):
    default_carrier_account: str
    r"""ID of the Carrier Account object to use as the default for all shipments in this Batch.
    The carrier account can be changed on a per-shipment basis by changing the carrier_account in the
    corresponding BatchShipment object.
    """
    default_servicelevel_token: str
    r"""Token of the service level to use as the default for all shipments in this Batch.
    The servicelevel can be changed on a per-shipment basis by changing the servicelevel_token in the
    corresponding BatchShipment object. <a href=\"#tag/Service-Levels\">Servicelevel tokens can be found here.</a>
    """
    batch_shipments: List[BatchShipmentCreateRequestTypedDict]
    r"""Array of BatchShipment objects. The response keeps the same order as in the request array."""
    label_filetype: NotRequired[LabelFileTypeEnum]
    r"""Print format of the <a href=\"https://docs.goshippo.com/docs/shipments/shippinglabelsizes/\">label</a>. If empty, will use the default format set from
    <a href=\"https://apps.goshippo.com/settings/labels\">the Shippo dashboard.</a>
    """
    metadata: NotRequired[str]
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""


class BatchCreateRequest(BaseModel):
    default_carrier_account: str
    r"""ID of the Carrier Account object to use as the default for all shipments in this Batch.
    The carrier account can be changed on a per-shipment basis by changing the carrier_account in the
    corresponding BatchShipment object.
    """

    default_servicelevel_token: str
    r"""Token of the service level to use as the default for all shipments in this Batch.
    The servicelevel can be changed on a per-shipment basis by changing the servicelevel_token in the
    corresponding BatchShipment object. <a href=\"#tag/Service-Levels\">Servicelevel tokens can be found here.</a>
    """

    batch_shipments: List[BatchShipmentCreateRequest]
    r"""Array of BatchShipment objects. The response keeps the same order as in the request array."""

    label_filetype: Optional[LabelFileTypeEnum] = None
    r"""Print format of the <a href=\"https://docs.goshippo.com/docs/shipments/shippinglabelsizes/\">label</a>. If empty, will use the default format set from
    <a href=\"https://apps.goshippo.com/settings/labels\">the Shippo dashboard.</a>
    """

    metadata: Optional[str] = None
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""
