from typing import Optional, List

from sqlalchemy.orm import Session
from core.crud import CRUDBase
from .models import __TEMPLATE_TABLENAME_CASE__, __TEMPLATE_TABLENAME_CASE__Create, __TEMPLATE_TABLENAME_CASE__Update


class CRUD__TEMPLATE_TABLENAME_CASE__(CRUDBase[__TEMPLATE_TABLENAME_CASE__, __TEMPLATE_TABLENAME_CASE__Create, __TEMPLATE_TABLENAME_CASE__Update]):
  # Declare model specific CRUD operation methods.
  pass


__TEMPLATE_TABLENAME_LOWER__ = CRUD__TEMPLATE_TABLENAME_CASE__(__TEMPLATE_TABLENAME_CASE__)
