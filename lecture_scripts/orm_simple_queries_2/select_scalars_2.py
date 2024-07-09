from sqlalchemy import select

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def select_workers_scalars():
    query = select(WorkerModel)

    with session_factory() as session:
        workers_fetchall = session.execute(query).fetchall()

        workers_scalars = session.execute(query).scalars().all()

        worker_scalar = session.execute(query).scalar()

        print(f'{workers_fetchall=}')
        print(f'{workers_scalars=}')
        print(f'{worker_scalar=}')


if __name__ == '__main__':
    create_table()
    fill_db()

    select_workers_scalars()
