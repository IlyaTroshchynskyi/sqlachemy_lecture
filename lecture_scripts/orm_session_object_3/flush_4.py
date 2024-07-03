from lecture_scripts.fill_db import line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def create_worker_auto_flush():
    """
    Flash is sent to db, but it is still not committed
    :return:
    """
    with session_factory(autoflush=False) as session:
        worker_jack = WorkerModel(username='Jack')
        print(worker_jack.id)

        session.add(worker_jack)
        print(worker_jack.id, 'Before flush')

        session.flush()
        print(worker_jack.id, 'after flush')

        session.commit()


if __name__ == '__main__':
    create_table()
    create_worker_auto_flush()
