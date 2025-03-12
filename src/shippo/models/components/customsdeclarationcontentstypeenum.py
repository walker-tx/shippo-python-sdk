"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class CustomsDeclarationContentsTypeEnum(str, Enum):
    r"""Type of goods of the shipment.
    Allowed values available <a href=\"#tag/Customs-Declaration-Contents-Type\">here</a>
    """

    DOCUMENTS = "DOCUMENTS"
    GIFT = "GIFT"
    SAMPLE = "SAMPLE"
    MERCHANDISE = "MERCHANDISE"
    HUMANITARIAN_DONATION = "HUMANITARIAN_DONATION"
    RETURN_MERCHANDISE = "RETURN_MERCHANDISE"
    OTHER = "OTHER"
