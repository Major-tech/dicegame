from dicegame.services.report_bug_service import report_bug_service
from dicegame.session.session_disk import Session


def report_bug_cmd(session: Session):
    """Returns the report bug service"""

    return report_bug_service(session)
