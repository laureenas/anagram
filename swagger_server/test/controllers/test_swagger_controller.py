# coding: utf-8
import pytest

@pytest.mark.xfail(reason='Not implemented yet')
def test_swagger_json_get(client):
    """Test case for swagger_json_get

    Show machine-readable API documentation.
    """
    response = client.get('/api/v1//swagger.json')
    assert response.status_code == 200
    assert response.json == {}
