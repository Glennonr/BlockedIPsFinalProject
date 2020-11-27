import App


def test_get():
    App.app.config['TESTING'] = True
    with App.app.test_client() as client:
        # Simulate the client calling GET /get
        # Capture the HTTP response
        response = client.get('/get').get_json()
        # assert the response message is correct
        expected = {'ips': []}
        assert response == expected
