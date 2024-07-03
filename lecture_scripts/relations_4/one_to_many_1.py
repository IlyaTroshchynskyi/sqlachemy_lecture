from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class WorkerModel(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64))

    resumes: Mapped[list['ResumeModel']] = relationship(back_populates='worker')


class ResumeModel(Base):
    __tablename__ = 'resumes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    compensation: Mapped[int | None] = mapped_column(Integer)
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete='CASCADE'))

    worker: Mapped['WorkerModel'] = relationship(back_populates='resumes')
