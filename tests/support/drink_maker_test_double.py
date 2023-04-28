class DrinkMakerTestDouble:
    def __init__(self):
        self.commands = []

    def run(self, command):
        self.commands.append(command)

    def get_received_commands(self):
        return self.commands[:]
