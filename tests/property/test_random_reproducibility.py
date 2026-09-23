from unipolar_sim.core.random import RandomStream


def test_seeded_random_stream_is_reproducible() -> None:
    a = RandomStream(seed=19920101)
    b = RandomStream(seed=19920101)
    assert [a.uniform(0, 1) for _ in range(10)] == [b.uniform(0, 1) for _ in range(10)]
