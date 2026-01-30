import pytest
from dicegame.commands.auth import(
    login_cmd,
    logout_cmd,
    signup_cmd
)
from dicegame.utils.dice_roll_utils import(
    SimpleDiceRollResult,
    PlayModeResult,
    GuessModeResult,
    RemovePlayerResult
)
from dicegame.commands.dice_roll import(
    simple_dice_roll_cmd,
    play_dice_roll_cmd,
    guess_dice_roll_cmd,
    reset_score_cmd
)
from dicegame.commands.player_delete import player_delete_cmd
from dicegame.services.leaderboard import(
    leaderboard_service,
    player_list_service
)
from dicegame.utils.errors import(
    UserNotFoundError,
    NotLoggedInError,
    AuthError,
    UserAlreadyExistsError
)
from dicegame.session.session_disk import Session


# Dummy session for testing
@pytest.fixture
def dummy_session():
    """Returns an empty dummy session for testing"""

    return Session(user_id= None,username= None,logged_in= False)


@pytest.fixture
def authenticated_session():
    """Returns a populated session for testing"""

    return Session(user_id= 1,username= 'testcase',logged_in= True)


# AUTHENTICATION COMMANDS
def test_login_cmd_wrong_credentials(dummy_session):
    """Verifies that a login attempt with wrong credentials raises a domain error"""

    with pytest.raises(UserNotFoundError):
        login_cmd('unknown','password',dummy_session)


def test_logout_cmd_inactive_session(dummy_session):
    """Verifies that logout works"""

    logout_cmd(dummy_session)


def test_signup__duplicate_account(dummy_session):
    """Verifies that attempts to create a duplicate account raise a domain error"""

    with pytest.raises(UserAlreadyExistsError):
        signup_cmd('testuser','pass123',dummy_session)



# GAME COMMANDS
# Simple dice roll
def test_simple_dice_roll_cmd_display(authenticated_session):
    """Verifies that the dice roll output is printed out correctly"""

    dice_roll: SimpleDiceRollResult = simple_dice_roll_cmd(4,authenticated_session)
    assert dice_roll.guess == 4


# Play mode
def test_play_dice_roll_cmd_success(authenticated_session):
    """Verifies that an output in range(4,6) in Play mode signifies a win"""

    dice_roll_win: PlayModeResult = play_dice_roll_cmd(5,authenticated_session)
    assert dice_roll_win.success


def test_play_dice_roll_cmd_fail(authenticated_session):
    """Verifies that an output in range(1,3) in Play mode signifies a user has lost"""

    dice_roll_fail: PlayModeResult  = play_dice_roll_cmd(2,authenticated_session)
    assert not dice_roll_fail.success


# Guess mode
def test_guess_dice_roll_cmd_valid_output(authenticated_session):
    """Verifies the dice roll output is always in range(1,6)"""

    dice_roll: GuessModeResult = guess_dice_roll_cmd(5,authenticated_session)
    assert dice_roll.lucky_number in range(1,7)



# PLAYER/LEADERBOARD COMMANDS
def test_player_list_service_valid_output(authenticated_session):
    """Ensure the service runs without errors"""

    player_list = player_list_service(authenticated_session)


def test_leaderboard_service_valid_output(authenticated_session):
    """Ensure the service runs without errors"""

    leaderboard = leaderboard_service(authenticated_session)


# RESET/DELETE COMMANDS
def test_player_delete_cmd_wrong_credentials(authenticated_session):
    with pytest.raises(UserNotFoundError):
        player_delete_cmd('password',authenticated_session)


def test_player_create_and_delete_success(dummy_session: Session):
    """Simulates signup ,login and deleting a player successfully"""

    # Test credentials
    username = 'testname2'
    password = 'Secret2'

    # Signup
    signup_session = signup_cmd(username,password,dummy_session)

    # Signup assertions
    assert signup_session.logged_in is True
    assert signup_session.username == username
    assert signup_session.user_id != None

    # User is automatically logged in after signup

    # Player delete
    player_delete: RemovePlayerResult = player_delete_cmd(password,signup_session)

    # Player delete assertions
    assert player_delete.success is True
    assert player_delete.username == username

    # Extra, illustrate that a deletion attempt on the deleted account fails

    with pytest.raises(UserNotFoundError):
        player_delete_cmd(password,signup_session)



