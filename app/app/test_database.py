from fastapi.testclient import TestClient

from . import crud
from .main import app


def test_post_items(db):
    client = TestClient(app)

    client.post("/items/", json={"title": "Item 1"})

    client.post("/items/", json={"title": "Item 2"})

    items = crud.get_items(db)
    assert len(items) == 2


def test_list_items(items, client):
    response = client.get("/items")
    assert len(response.json()) == 2
