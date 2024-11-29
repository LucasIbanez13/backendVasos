from app.game_logic import shuffle_positions

def test_shuffle_positions():
    positions = shuffle_positions()
    assert len(positions) == 3
    assert set(positions) == {1, 2, 3}
