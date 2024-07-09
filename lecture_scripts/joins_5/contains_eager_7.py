from sqlalchemy import select
from sqlalchemy.orm import contains_eager

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, ResumeModel, session_factory, WorkerModel


@line_separator
def select_workers_with_condition_relationship_contains_eager():
    """
    Allow to do order_by using another table
    :return:
    """
    query = (
        select(WorkerModel)
        .join(WorkerModel.resumes, isouter=True)
        .options(contains_eager(WorkerModel.resumes))
        .order_by(ResumeModel.title)
    )

    with session_factory() as session:
        workers = session.execute(query).unique().scalars().all()
        print(workers)
        print(workers[0].resumes)
        print(workers[1].resumes)


if __name__ == '__main__':
    create_table()
    fill_db()

    select_workers_with_condition_relationship_contains_eager()
