from __future__ import annotations

from typing import Generator
from unittest.mock import MagicMock, patch

import pytest

from deluge_web_client import DelugeWebClient


@pytest.fixture
def client_mock() -> Generator[tuple[DelugeWebClient, MagicMock], None, None]:
    """Fixture to initialize DelugeWebClient and mock its session."""
    with patch("niquests.Session.post") as mock_post:
        client = DelugeWebClient(
            url="http://mocked-deluge-url", password="mocked_password"
        )
        yield client, mock_post
