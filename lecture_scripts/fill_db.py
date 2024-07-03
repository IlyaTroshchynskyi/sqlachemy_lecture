from functools import wraps
from typing import Callable

from sqlalchemy import insert

from lecture_scripts.base_1.connection_3 import session_factory
from lecture_scripts.models import ResumeModel, VacanciesModel, WorkerModel


def fill_db():
    with session_factory() as session:
        workers = [
            {'username': 'Artem'},  # id 3
            {'username': 'Roman'},  # id 4
            {'username': 'Petr'},  # id 5
        ]
        resumes = [
            {'title': 'Python Dev', 'compensation': 60000, 'workload': 'full_time', 'worker_id': 1},
            {'title': 'Machine Learning Engineer', 'compensation': 70000, 'workload': 'part_time', 'worker_id': 1},
            {'title': 'Fullstack', 'compensation': 80000, 'workload': 'part_time', 'worker_id': 2},
            {'title': 'Python Analyst', 'compensation': 90000, 'workload': 'full_time', 'worker_id': 2},
            {'title': 'Angular Junior Developer', 'compensation': 100000, 'workload': 'full_time', 'worker_id': 3},
        ]
        insert_workers = insert(WorkerModel).values(workers)
        insert_resumes = insert(ResumeModel).values(resumes)

        session.execute(insert_workers)
        session.execute(insert_resumes)
        session.commit()

        new_vacancy = VacanciesModel(title='Python Dev', compensation=100000)
        resume_1 = session.get(ResumeModel, 1)
        resume_2 = session.get(ResumeModel, 2)
        resume_1.vacancies_replied.append(new_vacancy)
        resume_2.vacancies_replied.append(new_vacancy)
        session.commit()
    print('Db is filled', '=' * 130)


def line_separator(func: Callable):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f'{func.__name__}', '=' * 130)
        func(*args, **kwargs)

    return inner
