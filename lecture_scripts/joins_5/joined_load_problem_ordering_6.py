from sqlalchemy import select
from sqlalchemy.orm import joinedload

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, ResumeModel, session_factory, WorkerModel


@line_separator
def select_workers_with_joined_relationship_with_ordering():
    """
    Construct extra join
    :return:
    """
    query_error = select(WorkerModel).options(joinedload(WorkerModel.resumes)).order_by(ResumeModel.title)

    # Correct
    query_correct = (
        select(WorkerModel)
        .join(WorkerModel.resumes, isouter=True)
        .options(joinedload(WorkerModel.resumes))
        .order_by(ResumeModel.title)
    )

    with session_factory() as session:
        workers = session.execute(query_correct).unique().scalars().all()

        print(f'{workers[0].resumes=}')


if __name__ == '__main__':
    create_table()
    fill_db()

    select_workers_with_joined_relationship_with_ordering()
