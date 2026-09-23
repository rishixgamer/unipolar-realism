from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class FiscalState:
    """Minimal fiscal state used to establish accounting invariants.

    This is intentionally not a calibrated macro model. It exists so early development starts
    with explicit stock-flow accounting rather than free-form gameplay modifiers.
    """

    debt: Decimal
    primary_balance: Decimal
    interest_cost: Decimal
    stock_flow_adjustment: Decimal = Decimal("0")

    def next_debt(self) -> Decimal:
        """Return next-period debt.

        Convention: a positive primary_balance is a surplus; a negative value is a deficit.
        """

        return self.debt - self.primary_balance + self.interest_cost + self.stock_flow_adjustment
