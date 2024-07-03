from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def select_workers_one_or_none():
    """Raise an error"""
    query = select(WorkerModel)

    query_none = select(WorkerModel).filter(WorkerModel.id == 10_000)

    with session_factory() as session:
        error = 'No result'
        try:
            error = session.execute(query).one_or_none()
        except MultipleResultsFound as e:
            print(e)
        result_none = session.execute(query_none).one_or_none()

        print(f'{error=}')
        print(f'{result_none=}')


if __name__ == '__main__':
    create_table()
    fill_db()

    select_workers_one_or_none()
