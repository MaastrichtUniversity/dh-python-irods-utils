import re

import pytest

from dhpythonirodsutils import loggers
from dhpythonirodsutils.parsers import AUDIT_TRAIL_REGEX

MESSAGE_REGEX = (
    r"^\[(?P<time_stamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\]\s\[(?P<severity>\w*)\]"
    r"\s(?P<user>\w*)\s-\s(?P<message>.*)$"
)


@pytest.mark.parametrize(
    "severity, user, message",
    [
        ("Test1", "user1", "message!@#$%*()_+{}|:<>?"),
        ("1", "2", "3"),
    ],
)
def test_format_log_message(severity, user, message):
    log = loggers.format_log_message(severity, user, message)
    re_match = re.match(MESSAGE_REGEX, log)
    assert re_match
    assert severity.upper() == re_match.group("severity")
    assert user == re_match.group("user")
    assert message == re_match.group("message")


@pytest.mark.parametrize(
    "user, message",
    [
        ("user1", "message!@#$%*()_+{}|:<>?"),
        ("1", "2"),
    ],
)
def test_format_error_message(user, message):
    log = loggers.format_error_message(user, message)
    re_match = re.match(MESSAGE_REGEX, log)
    assert re_match
    assert "ERROR" == re_match.group("severity")
    assert user == re_match.group("user")
    assert message == re_match.group("message")


@pytest.mark.parametrize(
    "user, message",
    [
        ("user1", "message!@#$%*()_+{}|:<>?"),
        ("1", "2"),
    ],
)
def test_format_warning_message(user, message):
    log = loggers.format_warning_message(user, message)
    re_match = re.match(MESSAGE_REGEX, log)
    assert re_match
    assert "WARNING" == re_match.group("severity")
    assert user == re_match.group("user")
    assert message == re_match.group("message")


@pytest.mark.parametrize(
    "user_id, topic, event, expected_result",
    [
        ("user1", "topic", "message!@#$%*()_+{}|:<>?", False),
        (1, "hola", "2", True),
    ],
)
def test_format_audit_trail_message(user_id, topic, event, expected_result):
    log = loggers.format_audit_trail_message(user_id, topic, event)
    re_match = re.match(AUDIT_TRAIL_REGEX, log)
    assert re_match
    assert (str(user_id) == re_match.group("irods_user_id")) is expected_result
    assert topic.upper() == re_match.group("topic")
    assert event == re_match.group("event")
