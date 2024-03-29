"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import carrieraccountcanadapostcreaterequest as components_carrieraccountcanadapostcreaterequest
from ...models.components import carrieraccountchronopostcreaterequest as components_carrieraccountchronopostcreaterequest
from ...models.components import carrieraccountcolissimocreaterequest as components_carrieraccountcolissimocreaterequest
from ...models.components import carrieraccountcorreoscreaterequest as components_carrieraccountcorreoscreaterequest
from ...models.components import carrieraccountdeutschepostcreaterequest as components_carrieraccountdeutschepostcreaterequest
from ...models.components import carrieraccountdhlexpresscreaterequest as components_carrieraccountdhlexpresscreaterequest
from ...models.components import carrieraccountdpddecreaterequest as components_carrieraccountdpddecreaterequest
from ...models.components import carrieraccountdpdukcreaterequest as components_carrieraccountdpdukcreaterequest
from ...models.components import carrieraccounthermesukcreaterequest as components_carrieraccounthermesukcreaterequest
from ...models.components import carrieraccountposteitalianecreaterequest as components_carrieraccountposteitalianecreaterequest
from ...models.components import carrieraccountupscreaterequest as components_carrieraccountupscreaterequest
from ...models.components import carrieraccountuspscreaterequest as components_carrieraccountuspscreaterequest
from typing import Optional, Union


@dataclasses.dataclass
class RegisterCarrierAccountRequest:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    request_body: Optional[Union[components_carrieraccountcanadapostcreaterequest.CarrierAccountCanadaPostCreateRequest, components_carrieraccountchronopostcreaterequest.CarrierAccountChronopostCreateRequest, components_carrieraccountcolissimocreaterequest.CarrierAccountColissimoCreateRequest, components_carrieraccountcorreoscreaterequest.CarrierAccountCorreosCreateRequest, components_carrieraccountdeutschepostcreaterequest.CarrierAccountDeutschePostCreateRequest, components_carrieraccountdhlexpresscreaterequest.CarrierAccountDHLExpressCreateRequest, components_carrieraccountdpddecreaterequest.CarrierAccountDpdDeCreateRequest, components_carrieraccountdpdukcreaterequest.CarrierAccountDPDUKCreateRequest, components_carrieraccounthermesukcreaterequest.CarrierAccountHermesUKCreateRequest, components_carrieraccountposteitalianecreaterequest.CarrierAccountPosteItalianeCreateRequest, components_carrieraccountupscreaterequest.CarrierAccountUPSCreateRequest, components_carrieraccountuspscreaterequest.CarrierAccountUSPSCreateRequest]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Examples."""
    

