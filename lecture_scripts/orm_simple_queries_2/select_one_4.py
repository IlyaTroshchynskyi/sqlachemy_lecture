from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def select_workers_scalar_one(worker_id: int = 100000):
    """
    sqlalchemy.exc.NoResultFound: No row was found when one was required
    :return:
    """
    query = select(WorkerModel).filter(WorkerModel.id == worker_id)

    with session_factory() as session:
        try:
            result = 'No result'
            result = session.execute(query).scalar_one()
        except NoResultFound as e:
            print(e)

        print(result)


@line_separator
def select_workers_one(worker_id: int = 1):
    """vacancies_replies
    # Return one object, but it will be a tuple if it is multiple then we will have an error
    :return:
    """
    query = select(WorkerModel).filter(WorkerModel.id <= worker_id)

    with session_factory() as session:
        result = session.execute(query).one()

    print(f'select_workers_all = {result}')


if __name__ == '__main__':
    create_table()
    fill_db()

    select_workers_scalar_one()

    select_workers_one()
