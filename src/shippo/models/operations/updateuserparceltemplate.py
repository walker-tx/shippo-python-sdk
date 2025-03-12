"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from shippo.models.components import (
    userparceltemplateupdaterequest as components_userparceltemplateupdaterequest,
)
from shippo.types import BaseModel
from shippo.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateUserParcelTemplateGlobalsTypedDict(TypedDict):
    shippo_api_version: NotRequired[str]
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


class UpdateUserParcelTemplateGlobals(BaseModel):
    shippo_api_version: Annotated[
        Optional[str],
        pydantic.Field(alias="SHIPPO-API-VERSION"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


class UpdateUserParcelTemplateRequestTypedDict(TypedDict):
    user_parcel_template_object_id: str
    r"""Object ID of the user parcel template"""
    user_parcel_template_update_request: NotRequired[
        components_userparceltemplateupdaterequest.UserParcelTemplateUpdateRequestTypedDict
    ]


class UpdateUserParcelTemplateRequest(BaseModel):
    user_parcel_template_object_id: Annotated[
        str,
        pydantic.Field(alias="UserParcelTemplateObjectId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Object ID of the user parcel template"""

    user_parcel_template_update_request: Annotated[
        Optional[
            components_userparceltemplateupdaterequest.UserParcelTemplateUpdateRequest
        ],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
