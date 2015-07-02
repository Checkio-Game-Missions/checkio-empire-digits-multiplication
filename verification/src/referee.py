from checkio_referee import RefereeCodeGolf, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    DEFAULT_MAX_CODE_LENGTH = 100
    BASE_POINTS = 10
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
