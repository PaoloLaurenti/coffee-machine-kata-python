from coffee_machine_kata.beverage_request import BeverageRequest
from coffee_machine_kata.beverage_type import BeverageType
from coffee_machine_kata.coffee_machine import CoffeeMachine
from tests.support.drink_maker_test_double import DrinkMakerTestDouble

class TestCoffeeMachine:
    def test_dispense_tea_no_sugar(self):
        drink_maker_spy = DrinkMakerTestDouble()
        coffe_machine = CoffeeMachine(drink_maker_spy)

        beverage_request = BeverageRequest(beverage_type=BeverageType.TEA, sugar=0)
        coffe_machine.dispense(beverage_request)

        drink_maker_commands = drink_maker_spy.get_received_commands()
        assert len(drink_maker_commands) == 1
        assert drink_maker_commands[0] == "T::"

    def test_dispense_chocolate_no_sugar(self):
        drink_maker_spy = DrinkMakerTestDouble()
        coffe_machine = CoffeeMachine(drink_maker_spy)

        beverage_request = BeverageRequest(beverage_type=BeverageType.CHOCOLATE, sugar=0)
        coffe_machine.dispense(beverage_request)

        drink_maker_commands = drink_maker_spy.get_received_commands()
        assert len(drink_maker_commands) == 1
        assert drink_maker_commands[0] == "H::"

    def test_dispense_coffee_no_sugar(self):
        drink_maker_spy = DrinkMakerTestDouble()
        coffe_machine = CoffeeMachine(drink_maker_spy)

        beverage_request = BeverageRequest(beverage_type=BeverageType.COFFEE, sugar=0)
        coffe_machine.dispense(beverage_request)

        drink_maker_commands = drink_maker_spy.get_received_commands()
        assert len(drink_maker_commands) == 1
        assert drink_maker_commands[0] == "C::"
