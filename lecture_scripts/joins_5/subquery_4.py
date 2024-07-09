from sqlalchemy import select
from sqlalchemy.orm import subqueryload

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def select_workers_with_subquery():
    """ """
    query = select(WorkerModel).options(subqueryload(WorkerModel.resumes))

    with session_factory() as session:
        result = session.execute(query).scalars().all()

        worker_1_resumes = result[0].resumes
        print(worker_1_resumes)

        worker_2_resumes = result[1].resumes
        print(worker_2_resumes)


if __name__ == '__main__':
    create_table()
    fill_db()

    select_workers_with_subquery()
