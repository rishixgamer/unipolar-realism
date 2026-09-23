from __future__ import annotations

import random
from dataclasses import dataclass, field


@dataclass(slots=True)
class RandomStream:
    """Project-wide seeded random stream for reproducible scenarios."""

    seed: int
    _rng: random.Random = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._rng = random.Random(self.seed)

    def uniform(self, low: float, high: float) -> float:
        return self._rng.uniform(low, high)
