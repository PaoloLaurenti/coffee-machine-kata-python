from coffee_machine_kata.beverage_type import BeverageType


class CoffeeMachine:
    def __init__(self, drink_maker):
        self.drink_maker = drink_maker

    def dispense(self, beverage_request):
        drink_maker_command = self.build_drink_maker_command(beverage_request)
        self.drink_maker.run(drink_maker_command)

    def build_drink_maker_command(self, beverage_request):
        drink_maker_beverage = ""
        match beverage_request.beverage_type:
            case BeverageType.TEA:
                drink_maker_beverage = "T"
            case BeverageType.COFFEE:
                drink_maker_beverage = "C"
            case BeverageType.CHOCOLATE:
                drink_maker_beverage = "H"
        drink_maker_command = f"{drink_maker_beverage}::"
        return drink_maker_command
