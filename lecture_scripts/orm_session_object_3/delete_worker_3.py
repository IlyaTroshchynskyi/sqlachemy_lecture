from lecture_scripts.fill_db import line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def delete_worker():
    with session_factory() as session:
        worker_jack = WorkerModel(username='Jack')
        session.add(worker_jack)
        session.commit()

        session.delete(worker_jack)

        session.commit()

        worker_jack = session.get(WorkerModel, 1)
        print(f'{worker_jack=}')


if __name__ == '__main__':
    create_table()
    delete_worker()
