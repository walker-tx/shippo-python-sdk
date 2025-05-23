"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class TransactionStatusEnum(str, Enum):
    r"""Indicates the status of the Transaction."""

    WAITING = "WAITING"
    QUEUED = "QUEUED"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"
    REFUNDED = "REFUNDED"
    REFUNDPENDING = "REFUNDPENDING"
    REFUNDREJECTED = "REFUNDREJECTED"
