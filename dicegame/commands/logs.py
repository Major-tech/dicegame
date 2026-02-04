from dicegame.session.session_disk import Session
from dicegame.services.log_service import(
    view_logs_service,
    clear_logs_service
)
from dicegame.utils.errors import not_logged_in


def view_logs_cmd(session: Session) -> list:
    """Display all logs stored on disk"""

    # Ensure player is logged in
    not_logged_in(session)

    return view_logs_service(session)


def clear_logs_cmd(session: Session) -> bool | None:
    """Clear all log files stored on disk"""

    # Ensure player is logged in
    not_logged_in(session)

    return clear_logs_service(session)

