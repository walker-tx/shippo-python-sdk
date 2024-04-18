"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import trackingstatusenum as components_trackingstatusenum
from ...models.components import transactionstatusenum as components_transactionstatusenum
from typing import Optional


@dataclasses.dataclass
class ListTransactionsGlobals:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class ListTransactionsRequest:
    rate: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'rate', 'style': 'form', 'explode': True }})
    r"""Filter by rate ID"""
    object_status: Optional[components_transactionstatusenum.TransactionStatusEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'object_status', 'style': 'form', 'explode': True }})
    r"""Filter by object status"""
    tracking_status: Optional[components_trackingstatusenum.TrackingStatusEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tracking_status', 'style': 'form', 'explode': True }})
    r"""Filter by tracking status"""
    page: Optional[int] = dataclasses.field(default=1, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""The page number you want to select"""
    results: Optional[int] = dataclasses.field(default=25, metadata={'query_param': { 'field_name': 'results', 'style': 'form', 'explode': True }})
    r"""The number of results to return per page (max 100)"""
    

