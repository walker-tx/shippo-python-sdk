"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DefaultParcelTemplateUpdateRequestTypedDict(TypedDict):
    object_id: NotRequired[str]


class DefaultParcelTemplateUpdateRequest(BaseModel):
    object_id: Optional[str] = None
