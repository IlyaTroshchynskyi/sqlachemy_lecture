from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from lecture_scripts.base_1.base_class_1 import Base


class WorkerModel(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(64))
