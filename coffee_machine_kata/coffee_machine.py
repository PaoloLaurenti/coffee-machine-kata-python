from coffee_machine_kata.drink_maker_translator import DrinkMakerTranslator

class CoffeeMachine:
    def __init__(self, drink_maker):
        self.drink_maker = drink_maker
        self.drink_maker_translator = DrinkMakerTranslator()

    def dispense(self, beverage_request):
        drink_maker_command = self.drink_maker_translator.build_drink_maker_command(
            beverage_request.beverage_type,
            beverage_request.sugar)
        self.drink_maker.run(drink_maker_command)





