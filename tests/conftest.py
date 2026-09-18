from copy import deepcopy

import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def reset_activity_state():
    original_state = deepcopy(activities)
    activities.clear()
    activities.update(deepcopy(original_state))
    yield
    activities.clear()
    activities.update(deepcopy(original_state))
