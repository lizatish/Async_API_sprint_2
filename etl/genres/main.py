from elasticsearch import Elasticsearch
from psycopg2.extensions import connection as pg_connection

from common.components.elasticsearch_loader import ElasticsearchLoader
from common.components.producer import GenreProducer
from common.logger import get_logger
from common.postgres_utils import create_pg_connection
from common.state import State, JsonFileStorage
from genres.settings import conf
from genres.transform import Transform


def run_genres_etl(
        es: Elasticsearch,
        pg_conn: pg_connection,
        batch_size: int,
        state: State,
):
    """Запускает ETL-процесс для кинопроизведений.

    Args:
        es: Объект elasticsearch
        pg_conn: Соединение к postgres
        batch_size: Размер батча
        state: Хранилище состояния
    """
    producer = GenreProducer(pg_conn)
    transform = Transform()
    elastic_saver = ElasticsearchLoader(es, conf.elastic_index_name, conf.index_json_path)

    latest_genres_state = state.get_state(conf.table_name)

    genres_producer = producer.load_data(batch_size, latest_genres_state)
    for producers_batch in genres_producer:
        genres_list = list(producers_batch)

        transform.create_documents(genres_list)
        elastic_saver.write_to_index(
            transform.base_dict.values(),
        )

        state.set_state(
            conf.table_name,
            genres_list[-1].updated_at.isoformat(),
        )


def main():
    """Главная функция запуска приложения."""
    dsl = {
        'dbname': conf.POSTGRES_DB_NAME,
        'user': conf.POSTGRES_DB_USER,
        'password': conf.POSTGRES_DB_PASSWORD,
        'host': conf.POSTGRES_DB_HOST,
        'port': conf.POSTGRES_DB_PORT,
    }
    pg_conn = create_pg_connection(dsl)

    storage = JsonFileStorage(conf.PATH_TO_STORAGE_JSON)
    state = State(storage)
    portion_size = conf.DATA_BATCH_SIZE
    es = Elasticsearch(f"http://{conf.ELASTIC_HOST}:{conf.ELASTIC_PORT}")
    get_logger().error(f"ELASTIC http://{conf.ELASTIC_HOST}:{conf.ELASTIC_PORT}")
    with pg_conn:
        while True:
            run_genres_etl(es, pg_conn, portion_size, state)
    pg_conn.close()


if __name__ == '__main__':
    main()
