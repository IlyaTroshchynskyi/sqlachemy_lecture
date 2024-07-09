from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class WorkerModel(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(64))
    resumes: Mapped[list['ResumeModel']] = relationship(back_populates='worker')

    resumes_part_time: Mapped[list['ResumeModel']] = relationship(
        # backref - creates a relationship implicitly, i.e. it is not necessary to register it in the second table.
        # backref='worker',
        back_populates='worker',
        primaryjoin="and_(WorkerModel.id == ResumeModel.worker_id, ResumeModel.workload == 'part_time')",
        order_by='ResumesOrm.id.desc()',
        viewonly=True,
        lazy='selectin',
    )


class ResumeModel(Base):
    __tablename__ = 'resumes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete='CASCADE'))

    worker: Mapped['WorkerModel'] = relationship(back_populates='resumes')
