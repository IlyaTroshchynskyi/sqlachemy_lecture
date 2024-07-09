from lecture_scripts.fill_db import line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def insert_workers():
    with session_factory(expire_on_commit=False) as session:
        worker_jack = WorkerModel(username='Jack')
        worker_michael = WorkerModel(username='Michael')
        session.add_all([worker_jack, worker_michael])
        session.flush()
        print(worker_jack)
        session.commit()


if __name__ == '__main__':
    create_table()
    insert_workers()
