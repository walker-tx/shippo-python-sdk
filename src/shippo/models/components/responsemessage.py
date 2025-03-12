"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ResponseMessageTypedDict(TypedDict):
    r"""Message returned with supporting information from a request. In some cases this can be an error message,
    for example a timeout from a carrier. If available, the origin of the message is displayed in `source`.
    """

    source: NotRequired[str]
    r"""Origin of message"""
    code: NotRequired[str]
    r"""Classification of message"""
    text: NotRequired[str]
    r"""Message content"""


class ResponseMessage(BaseModel):
    r"""Message returned with supporting information from a request. In some cases this can be an error message,
    for example a timeout from a carrier. If available, the origin of the message is displayed in `source`.
    """

    source: Optional[str] = None
    r"""Origin of message"""

    code: Optional[str] = None
    r"""Classification of message"""

    text: Optional[str] = None
    r"""Message content"""
