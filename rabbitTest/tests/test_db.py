import asyncio
import pytest
from unittest.mock import patch, MagicMock
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession
from hello.db.dependencies import (
    get_db_session,
)  # Replace with your actual module and function


class MockAsyncSession:
    async def commit(self):
        pass

    async def close(self):
        pass


@pytest.mark.asyncio
@patch("hello.db.dependencies.AsyncSession", new=MockAsyncSession)
async def test_get_db_session():
    request_mock = MagicMock()
    request_mock.app.state.db_session_factory = lambda: AsyncSession()

    async for session in get_db_session(request_mock):
        assert isinstance(session, AsyncSession)
    assert session is not AsyncSession
