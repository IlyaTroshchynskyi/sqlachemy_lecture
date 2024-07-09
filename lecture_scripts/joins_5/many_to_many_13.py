from sqlalchemy import select
from sqlalchemy.orm import selectinload

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, ResumeModel, session_factory, VacanciesModel


@line_separator
def select_resumes_and_vacancies():
    query = select(ResumeModel).options(selectinload(ResumeModel.vacancies_replied).load_only(VacanciesModel.title))

    with session_factory() as session:
        resumes = session.execute(query).scalars().all()
        print(f'{resumes=}')
        print(f'{resumes[0].vacancies_replied=}')


if __name__ == '__main__':
    create_table()
    fill_db()
    select_resumes_and_vacancies()
