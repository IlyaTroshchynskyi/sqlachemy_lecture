from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def get_worker_refresh():
    """
    Refresh is needed if we want to reload the model data from the database.
    Suitable if we received the model a long time ago and at that time the data in the
    database could have been changed
    """
    with session_factory() as session:
        worker_jack = session.get(WorkerModel, 1)

        worker_jack.username = 'Updated'
        print('Before refresh=', worker_jack.username)

        session.refresh(worker_jack)

        print('After refresh=', worker_jack.username)
        session.commit()
        print('After commit =====================================')
        worker = session.get(WorkerModel, worker_jack.id)
        print(worker)


if __name__ == '__main__':
    create_table()
    fill_db()
    get_worker_refresh()
