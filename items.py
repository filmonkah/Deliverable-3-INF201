from Dice import Dice



class Weapon:
    """Represent a weapon that uses dice to calculate damage."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initializ a weapon
        
        Args:
            name (str) Name of the weapon.
            damage_dice (Dice) Dice used to calculate damage.
            """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon`s damage dice and return the result."""
        return self.damage_dice.roll()