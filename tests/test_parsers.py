import pytest

from dhpythonirodsutils import parsers


@pytest.mark.parametrize(
    "log, expected_result",
    [
        ("[2022-05-03 16:37:23][AUDIT_TRAIL][10043][EXPORT_DATAVERSE] - Dataverse", True),
        ("[2022-05-03 16:12:12][AUDIT_TRAIL][10043][CREATE_DROPZONE] - type: direct. User is internal: False", True),
        ("[2022-05-03 16:12:10][AUDIT_TRAIL][][] - False", True),
        ("wrong", False),
        ("[2022-05-03 16:12:11][AUDIT_TRAIL][][CREATE_DROPZONE]-False", False),
        ("[2022-05-03 16:12:12][AUDIT_TRAIL][][CREATE_DROPZONE]- False", False),
        ("[2022-05-03][AUDIT_TRAIL][10043][CREATE_DROPZONE] - False", False),
        ("[2022-05-03 16:49:30][AUDIT_TRAIL][10043][DOWNLOAD_DATA] - downloaded ", True),
        (
            "[2022-05-03 16:53:21][AUDIT_TRAIL][jmelius][DOWNLOAD_DATA] - GET /P000000017/C000000001/ncit.owl HTTP/1.1",
            True,
        ),
    ],
)
def test_parse_audit_trail_message(log, expected_result):
    result = True
    try:
        parsers.parse_audit_trail_message(log)
    except ValueError:
        result = False
    assert result is expected_result
