from dicegame.services.report_bug_service import report_bug_service
from dicegame.session.session_disk import Session
from dicegame.utils.errors import not_logged_in


def report_bug_cmd(session: Session):
    """Returns the report bug service"""

    # Ensure player is logged in
    not_logged_in(session)

    return report_bug_service(session)
