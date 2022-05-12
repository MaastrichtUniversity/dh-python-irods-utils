import re
from datetime import datetime

AUDIT_TRAIL_REGEX = (
    r"^\[(?P<time_stamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\]\[AUDIT_TRAIL\]"
    r"(\[(?P<irods_user_id>\d*)\]|\[(?P<irods_user_name>\w*)\])\[(?P<topic>.*)\]\s-\s(?P<event>.*)$"
)


def parse_audit_trail_message(message, parse_time_stamp=False):
    """
    Parameters
    ----------
    message: str
        Audit log message
    parse_time_stamp: bool
        Whether to parse time_stamp to a python datetime object or not

    Returns
    -------
    dict
        Parsed audit log with following keys:
            time_stamp
            irods_user_id
            topic
            event
    """
    re_match = re.match(AUDIT_TRAIL_REGEX, message)
    if re_match:
        output = {}
        if parse_time_stamp:
            output["time_stamp"] = datetime.strptime(re_match.group("time_stamp"), "%Y-%m-%d %H:%M:%S")
        else:
            output["time_stamp"] = re_match.group("time_stamp")
        output["irods_user_id"] = re_match.group("irods_user_id")
        output["irods_user_name"] = re_match.group("irods_user_name")
        output["topic"] = re_match.group("topic")
        output["event"] = re_match.group("event")
        return output

    raise ValueError("No Match found. Unable to parse Audit log message")
