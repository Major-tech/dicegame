import pytest
from dicegame.session.session_disk import Session
from dicegame.utils.security import generate_session_token
from dicegame.utils.dice_roll_utils import(
    get_random_number,
    play_mode_dice_roll_result,
)

@pytest.fixture
def dummy_session():
    """Returns a dummy session for testing"""

    return Session(user_id= 1,username= 'testuser',logged_in= True)


def test_generate_session_token():
    token = generate_session_token()

    assert isinstance(token,str)


def test_get_random_number():
    number = get_random_number()

    assert isinstance(number,int)


def test_play_mode_dice_roll_result(dummy_session):
    guess = play_mode_dice_roll_result(dummy_session)

    assert guess in range(1,7)
