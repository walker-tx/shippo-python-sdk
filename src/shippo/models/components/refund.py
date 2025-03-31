"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RefundStatus(str, Enum):
    r"""Indicates the status of the Refund."""

    QUEUED = "QUEUED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"


class RefundTypedDict(TypedDict):
    object_created: NotRequired[datetime]
    r"""Date and time of object creation."""
    object_id: NotRequired[str]
    r"""Unique identifier of the given object."""
    object_owner: NotRequired[str]
    r"""Username of the user who created the object."""
    object_updated: NotRequired[datetime]
    r"""Date and time of last object update."""
    status: NotRequired[RefundStatus]
    r"""Indicates the status of the Refund."""
    test: NotRequired[bool]
    r"""Indicates whether the object has been created in test mode."""
    transaction: NotRequired[str]
    r"""Object ID of the Transaction to be refunded."""


class Refund(BaseModel):
    object_created: Optional[datetime] = None
    r"""Date and time of object creation."""

    object_id: Optional[str] = None
    r"""Unique identifier of the given object."""

    object_owner: Optional[str] = None
    r"""Username of the user who created the object."""

    object_updated: Optional[datetime] = None
    r"""Date and time of last object update."""

    status: Optional[RefundStatus] = None
    r"""Indicates the status of the Refund."""

    test: Optional[bool] = None
    r"""Indicates whether the object has been created in test mode."""

    transaction: Optional[str] = None
    r"""Object ID of the Transaction to be refunded."""
