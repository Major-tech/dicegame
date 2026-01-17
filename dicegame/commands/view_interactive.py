from dicegame.services.view import(
    view_users_service,
    view_scores_service
)


def view_users_cmd_interactive(session):
    view_users_service()


def view_scores_cmd_interactive(session):
    view_scores_service()

