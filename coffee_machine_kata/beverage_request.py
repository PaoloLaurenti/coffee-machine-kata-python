from dataclasses import dataclass
from coffee_machine_kata.beverage_type import BeverageType

@dataclass(frozen=True)
class BeverageRequest:
    beverage_type: BeverageType
    sugar: int
