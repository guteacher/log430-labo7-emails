"""
Tests for Coolriel
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from datetime import datetime
from handlers.user_created_handler import UserCreatedHandler
from handlers.user_deleted_handler import UserDeletedHandler


def test_user_created_handler():
    user_creation = UserCreatedHandler()
    mock_event = {
        "id": 998,
        "name": 'Joanne Test',
        "email": 'joannetest@example.com',
        "datetime": str(datetime.now())
    }
    user_creation.handle(mock_event)

def test_user_deleted_handler():
    user_creation = UserDeletedHandler()
    mock_event = {
        "id": 999,
        "name": 'Joe Test',
        "email": 'joetest@example.com',
        "datetime": str(datetime.now())
    }
    user_creation.handle(mock_event)