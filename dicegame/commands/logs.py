from dicegame.session.session_disk import Session
from dicegame.services.log_service import(
    view_logs_service,
    clear_logs_service
)


def view_logs_cmd(session: Session) -> list:
    """Display all logs stored on disk"""

    return view_logs_service(session)


def clear_logs_cmd(session: Session):
    """Clear all log files stored on disk"""

    return clear_logs_service(session)

