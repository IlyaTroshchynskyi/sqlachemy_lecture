from sqlalchemy import select
from sqlalchemy.orm import joinedload

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def select_workers_with_joined_relationship():
    """
    Will be loaded all records
    has prop innerjoin=True
    :return:
    """
    query = select(WorkerModel).options(joinedload(WorkerModel.resumes))

    with session_factory() as session:
        workers = session.execute(query).unique().scalars().all()
        # unique() is important because we wil have dublications. It is done on the level sqlachemy
        print(workers)
        worker_1_resumes = workers[0].resumes
        print(worker_1_resumes)

        worker_2_resumes = workers[1].resumes
        print(worker_2_resumes)


if __name__ == '__main__':
    create_table()
    fill_db()

    select_workers_with_joined_relationship()
