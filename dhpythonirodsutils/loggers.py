import datetime


def format_log_message(severity, user, message):
    """
    Format a log message with variable severity

    Parameters
    ----------
    severity
        The severity of the log
    user
        The user triggering the message
    message
        The message to log

    Returns
    -------
        The string of the formatted log message
    """
    return "[%s] [%s] %s - %s" % (
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"),
        severity.upper(),
        user,
        message,
    )


def format_error_message(user, message):
    """
    Format a log message with severity "error"

    Parameters
    ----------
    user
        The user triggering the message
    message
        The message to log

    Returns
    -------
        The string of the formatted log message
    """
    return format_log_message("ERROR", user, message)


def format_warning_message(user, message):
    """
    Format a log message with severity "warning"

    Parameters
    ----------
    user
        The user triggering the message
    message
        The message to log

    Returns
    -------
        The string of the formatted log message
    """
    return format_log_message("WARNING", user, message)


def format_audit_trail_message(user_id, topic: str, event):
    """
    Log an entry with AUDIT_TRAIL tag and user ID

    Parameters
    ----------
    user_id: int
        The user identifier number
    topic: str
        The General topic for this log
    event: str
        The event you want to be logged

    """
    if type(user_id) != int:
        user_id = ""
    return "[%s][AUDIT_TRAIL][%s][%s] - %s" % (
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"),
        str(user_id),
        str(topic).upper(),
        event,
    )
