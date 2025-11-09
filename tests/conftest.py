from unittest.mock import patch

import pytest

from deluge_web_client import DelugeWebClient


@pytest.fixture
def client_mock():
    """Fixture to initialize DelugeWebClient and mock its session."""
    with patch("niquests.Session.post") as mock_post:
        client = DelugeWebClient(
            url="http://mocked-deluge-url", password="mocked_password"
        )
        yield client, mock_post
