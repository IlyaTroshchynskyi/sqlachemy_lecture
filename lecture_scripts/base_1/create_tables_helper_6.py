from lecture_scripts.base_1.base_class_with_annotation_4 import Base
from lecture_scripts.base_1.connection_3 import sync_engine


def create_table():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


if __name__ == '__main__':
    """
    Need import from lecture_scripts.base_1.simple_model_with_annotation_5 import WorkerModel
    """
    create_table()
