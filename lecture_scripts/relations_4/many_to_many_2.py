from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class ResumeModel(Base):
    __tablename__ = 'resumes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256))

    vacancies: Mapped[list['VacanciesModel']] = relationship(
        back_populates='resumes',
        secondary='vacancies_replies',
    )


class VacanciesModel(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    compensation: Mapped[int | None] = mapped_column(Integer)

    resumes: Mapped[list['ResumeModel']] = relationship(
        back_populates='vacancies',
        secondary='vacancies_replies',
    )


class VacanciesRepliesModel(Base):
    __tablename__ = 'vacancies_replies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    resume_id: Mapped[int] = mapped_column(
        ForeignKey('resumes.id', ondelete='CASCADE'),
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey('vacancies.id', ondelete='CASCADE'),
    )

    cover_letter: Mapped[str | None]
