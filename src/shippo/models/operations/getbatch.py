"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class GetBatchGlobals:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class GetBatchRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'BatchId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the batch"""
    

