# coding: utf-8

def test_version_get(client):
    """Test case for version_get

    Return API version.
    """
    response = client.get('/api/v1/version')
    assert response.status_code == 200
    assert response.json == {'version': '0.1.0'}
