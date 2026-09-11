"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


# TODO 2: test_matches_law
def test_matches_law():
    N0, lam, dt = 1000, 0.4, 0.05
    step = 20  # step * dt = 1.0 second real time
    T = step * dt
    results = [simulate(N0, lam, dt=dt, seed=s)[step] for s in range(300)]
    avg = np.mean(results)
    expected = N0 * np.exp(-lam * T)
    assert avg == pytest.approx(expected, rel=0.1)
