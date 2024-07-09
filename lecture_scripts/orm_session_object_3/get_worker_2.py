from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def get_worker():
    with session_factory() as session:
        worker = session.get(WorkerModel, 1)

        print(f'result={worker}')


if __name__ == '__main__':
    create_table()
    fill_db()
    get_worker()
