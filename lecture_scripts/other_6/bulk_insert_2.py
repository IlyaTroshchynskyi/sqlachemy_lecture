from sqlalchemy import insert, select

from lecture_scripts.models import create_table, ResumeModel, session_factory, WorkerModel


def bulk_insert():
    workers = [
        {'username': 'Artem'},
        {'username': 'Roman'},
        {'username': 'Petr'},
    ]
    insert_workers_query = insert(WorkerModel).values(workers)

    with session_factory() as session:
        session.execute(insert_workers_query)
        session.commit()

        query = (
            insert(ResumeModel)
            .values(
                [
                    {
                        'title': 'Test1',
                        'workload': 'part_time',
                        'worker_id': select(WorkerModel.id).where(WorkerModel.username == 'Roman'),
                    },
                    {
                        'title': 'Test2',
                        'workload': 'part_time',
                        'worker_id': select(WorkerModel.id).where(WorkerModel.username == 'Petr'),
                    },
                ]
            )
            .returning(ResumeModel)
        )

    result = session.execute(query).scalars().all()
    print(result)


if __name__ == '__main__':
    create_table()
    bulk_insert()
