from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def get_worker_expire():
    """
    Expire will delete all changes in session. However, no extra queries.
    Method will erase the contents of selected or all attributes of an object, such that they will be loaded from the
    database when they are next accessed, e.g. using a lazy loading pattern:

    The Session uses the expiration feature automatically whenever the transaction referred to by the session ends.
     Meaning, whenever Session.commit() or Session.rollback() is called, all objects within the Session are expired,
     using a feature equivalent to that of the Session.expire_all() method
    """
    with session_factory() as session:
        worker_jack = session.get(WorkerModel, 1)

        worker_jack.username = 'Updated'
        print('Before expire', worker_jack)
        session.expire(worker_jack)
        print('After expire=', worker_jack.username)
        session.commit()


if __name__ == '__main__':
    create_table()
    fill_db()
    get_worker_expire()
