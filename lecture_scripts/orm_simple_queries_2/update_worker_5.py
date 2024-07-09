from sqlalchemy import update

from lecture_scripts.fill_db import fill_db, line_separator
from lecture_scripts.models import create_table, session_factory, WorkerModel


@line_separator
def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
    query = update(WorkerModel).values(username=new_username).filter(WorkerModel.id == worker_id).returning(WorkerModel)

    with session_factory() as session:
        worker_updated = session.execute(query).scalar()
        print(worker_updated)
        session.commit()


if __name__ == '__main__':
    create_table()
    fill_db()

    update_worker(new_username='Test_username')
