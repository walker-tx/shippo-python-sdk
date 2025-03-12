"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class TrackingStatusEnum(str, Enum):
    r"""Indicates the high level status of the shipment."""

    UNKNOWN = "UNKNOWN"
    PRE_TRANSIT = "PRE_TRANSIT"
    TRANSIT = "TRANSIT"
    DELIVERED = "DELIVERED"
    RETURNED = "RETURNED"
    FAILURE = "FAILURE"
