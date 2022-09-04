from typing import List


def get_es_fw_bulk_query(es_data: List, es_index: str, es_id_field: str):
    for doc in es_data:
        yield {
            '_op_type': 'index',
            '_id': doc[es_id_field],
            '_index': es_index,
            '_source': doc,
        }
