import pytest
from coffee_machine_kata.beverage_request import BeverageRequest
from coffee_machine_kata.beverage_type import BeverageType
from coffee_machine_kata.coffee_machine import CoffeeMachine
from tests.support.drink_maker_test_double import DrinkMakerTestDouble


class TestCoffeeMachine:
    @pytest.mark.parametrize(
        "beverage_type, expected_command",
        [
            (BeverageType.TEA, "T::"),
            (BeverageType.COFFEE, "C::"),
            (BeverageType.CHOCOLATE, "H::"),
        ],
    )
    def test_dispense_beverage_no_sugar(self, beverage_type, expected_command):
        drink_maker_spy = DrinkMakerTestDouble()
        coffe_machine = CoffeeMachine(drink_maker_spy)

        beverage_request = BeverageRequest(beverage_type=beverage_type, sugar=0)
        coffe_machine.dispense(beverage_request)

        drink_maker_commands = drink_maker_spy.get_received_commands()
        assert len(drink_maker_commands) == 1
        assert drink_maker_commands[0] == expected_command

