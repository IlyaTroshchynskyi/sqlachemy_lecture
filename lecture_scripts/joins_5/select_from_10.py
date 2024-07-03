from sqlalchemy import func, select

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def select_from_func():
    query = select(func.count()).select_from(WorkerModel)

    with session_factory() as session:
        count = session.execute(query).scalar()
        print(f'{count=}')


if __name__ == '__main__':
    create_table()
    fill_db()

    select_from_func()
