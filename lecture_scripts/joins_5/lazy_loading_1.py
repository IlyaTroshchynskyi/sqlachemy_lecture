from sqlalchemy import select

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def select_workers_with_lazy_relationship():
    """
    Here we have problem N+1. When trying to get a resume for new workers, sqlachemy executes a new query
    It is called lazy loading
    :return:
    """
    query = select(WorkerModel)

    with session_factory() as session:
        workers = session.execute(query).scalars().all()

        for worker in workers:
            print(worker.resumes)


if __name__ == '__main__':
    create_table()
    fill_db()

    select_workers_with_lazy_relationship()
