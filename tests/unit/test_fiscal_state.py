from decimal import Decimal

from unipolar_sim.core.state import FiscalState


def test_debt_stock_flow_identity_with_deficit() -> None:
    state = FiscalState(
        debt=Decimal("100"),
        primary_balance=Decimal("-5"),
        interest_cost=Decimal("3"),
        stock_flow_adjustment=Decimal("1"),
    )
    assert state.next_debt() == Decimal("109")


def test_surplus_reduces_debt_all_else_equal() -> None:
    state = FiscalState(
        debt=Decimal("100"),
        primary_balance=Decimal("10"),
        interest_cost=Decimal("0"),
    )
    assert state.next_debt() == Decimal("90")
