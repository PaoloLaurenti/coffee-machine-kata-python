from coffee_machine_kata.beverage_type import BeverageType


class CoffeeMachine:
    def __init__(self, drink_maker):
        self.drink_maker = drink_maker

    def dispense(self, beverage_request):
        drink_maker_beverage = ""
        match beverage_request.beverage_type:
            case BeverageType.TEA:
                drink_maker_beverage = "T"
            case BeverageType.COFFEE:
                drink_maker_beverage = "C"
            case BeverageType.CHOCOLATE:
                drink_maker_beverage = "H"
        self.drink_maker.run(f"{drink_maker_beverage}::")
