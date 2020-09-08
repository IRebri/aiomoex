from aiomoex import request_helpers


def test_make_query_empty():
    query = request_helpers.make_query()
    assert query == {}


def test_make_query_full():
    query = request_helpers.make_query(start=1, end=2, table=3, columns=("4",))
    assert isinstance(query, dict)
    assert len(query) == 4
    assert query["from"] == 1
    assert query["till"] == 2
    assert query["iss.only"] == f"3,history.cursor"
    assert query[f"{3}.columns"] == "4"


def test_make_query_many_columns():
    query = request_helpers.make_query(table=1, columns=("2", "3"))
    assert isinstance(query, dict)
    assert len(query) == 2
    assert query["iss.only"] == f"1,history.cursor"
    assert query[f"{1}.columns"] == "2,3"
