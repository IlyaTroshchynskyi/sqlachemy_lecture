from sqlalchemy import insert

from lecture_scripts.fill_db import line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def insert_workers():
    query = insert(WorkerModel).values(username='Jack').returning(WorkerModel)

    with session_factory() as session:
        worker = session.execute(query).scalar()
        print(worker)
        session.commit()


if __name__ == '__main__':
    create_table()
    insert_workers()
