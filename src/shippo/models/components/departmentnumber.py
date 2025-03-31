"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DepartmentNumberTypedDict(TypedDict):
    r"""Specify the department number field on the label (FedEx and UPS only)."""

    prefix: NotRequired[str]
    r"""Custom prefix for department number field (ZPL labels only). Up to 11 characters, including trailing
    spaces. Empty string indicates removal of default prefix. To use the default prefix, do not include
    this property.
    """
    value: NotRequired[str]
    r"""Optional text to be printed on the shipping label for department number. Up to 40 characters."""
    ref_sort: NotRequired[int]
    r"""Order UPS reference fields are printed on ZPL labels. For UPS shipments, if you choose to set `ref_sort` for one reference, you must set `ref_sort` for all other supported UPS references using unique integers."""


class DepartmentNumber(BaseModel):
    r"""Specify the department number field on the label (FedEx and UPS only)."""

    prefix: Optional[str] = None
    r"""Custom prefix for department number field (ZPL labels only). Up to 11 characters, including trailing
    spaces. Empty string indicates removal of default prefix. To use the default prefix, do not include
    this property.
    """

    value: Optional[str] = None
    r"""Optional text to be printed on the shipping label for department number. Up to 40 characters."""

    ref_sort: Optional[int] = None
    r"""Order UPS reference fields are printed on ZPL labels. For UPS shipments, if you choose to set `ref_sort` for one reference, you must set `ref_sort` for all other supported UPS references using unique integers."""
