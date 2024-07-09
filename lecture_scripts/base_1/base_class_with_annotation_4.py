import datetime
import decimal
from decimal import Decimal
from typing import Annotated
from uuid import UUID

from sqlalchemy import Boolean, Date, DateTime, Float, Integer, Interval, LargeBinary, Numeric, String, Time, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

str_256 = Annotated[str, 256]
num_12_4 = Annotated[Decimal, 12]


class Base(DeclarativeBase):
    type_annotation_map = {str_256: String(256), num_12_4: Numeric(12, 4)}


class WorkerModel(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str_256]
    address: Mapped[str | None] = mapped_column(nullable=False)  # will be String() NOT NULL, but can be None in Python
    salary: Mapped[num_12_4]


# default type mapping, deriving the type for mapped_column() from a Mapped[] annotation
type_map = {
    bool: Boolean(),
    bytes: LargeBinary(),
    datetime.date: Date(),
    datetime.datetime: DateTime(),
    datetime.time: Time(),
    datetime.timedelta: Interval(),
    decimal.Decimal: Numeric(),
    float: Float(),
    int: Integer(),
    str: String(),
    UUID: Uuid(),
}
