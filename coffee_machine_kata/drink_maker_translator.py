from coffee_machine_kata.beverage_type import BeverageType


class DrinkMakerTranslator:
    def build_drink_maker_command(self, beverage_type, sugar):
        drink_maker_beverage = self.get_drink_maker_beverage_command(beverage_type)
        drink_maker_sugar = self.get_drink_maker_sugar_command(sugar)
        return f"{drink_maker_beverage}:{drink_maker_sugar}:"

    def get_drink_maker_beverage_command(self, beverage_type):
        drink_maker_beverage = ""
        match beverage_type:
            case BeverageType.TEA:
                drink_maker_beverage = "T"
            case BeverageType.COFFEE:
                drink_maker_beverage = "C"
            case BeverageType.CHOCOLATE:
                drink_maker_beverage = "H"
        return drink_maker_beverage

    def get_drink_maker_sugar_command(self, sugar):
        drink_maker_sugar = ""
        match sugar:
            case 1:
                drink_maker_sugar = "1"
            case 2:
                drink_maker_sugar = "2"
        return drink_maker_sugar
