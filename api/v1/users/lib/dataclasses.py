from dataclasses import dataclass
from typing import Union, Any, Dict, Optional
from datetime import datetime
from decimal import Decimal
from uuid import UUID


@dataclass
class EmployeeData:
    uuid: Union[UUID, str]
    id: int
    birth_date: datetime
    photo: Optional[str]
    date_joined: datetime
    last_modified: datetime
    phone: str
    street: str
    state: str
    city: str
    neighborhood: str
    zip_code: str
    salary: Decimal()
