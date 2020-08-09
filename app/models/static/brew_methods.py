class BrewMethod:

    def __init__(self, name: str):
        self.name = name


class BrewMethods:
    CUPPING = BrewMethod('cupping')
    POUR_OVER = BrewMethod('pour_over')
    FRENCH_PRESS = BrewMethod('french_press')
    ESPRESSO = BrewMethod('espresso')
    SIPHON = BrewMethod('siphon')
    COLD_BREW = BrewMethod('cold_brew')
    AEROPRESS = BrewMethod('aeropress')
