"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import userparceltemplateupdaterequest as components_userparceltemplateupdaterequest
from typing import Optional


@dataclasses.dataclass
class UpdateUserParcelTemplateGlobals:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class UpdateUserParcelTemplateRequest:
    user_parcel_template_object_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'UserParcelTemplateObjectId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the user parcel template"""
    user_parcel_template_update_request: Optional[components_userparceltemplateupdaterequest.UserParcelTemplateUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

