import datetime


def format_log_message(severity, user, message):
    return (
        "[%s] [%s] %s - %s",
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"),
        severity.upper(),
        user,
        message,
    )


def format_error_message(user, message):
    return format_log_message("ERROR", user, message)


def format_warning_message(user, message):
    return format_log_message("WARNING", user, message)


def format_audit_trail_message(user_id, event):
    """
    Log an entry with AUDIT_TRAIL tag and user ID

    Parameters
    ----------
    user_id: int
        The user identifier number
    event: str
        The event you want to be logged

    """
    if type(user_id) != int:
        user_id = ""
    return (
        "[%s][AUDIT_TRAIL][USER_ID %s] - %s",
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"),
        str(user_id),
        event,
    )
