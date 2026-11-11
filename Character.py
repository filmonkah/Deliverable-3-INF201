from items import Weapon

# Object-oriented game simulator
# Turid Torheim, NMBU, 2026


class Character:
    """Represents a character in the RPG"""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        ) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): Optional equipped weapon (default = None).
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """ 
        Reduce the character`s HP by the given amount.

        HP cannot fall below zero.
        
        Args:
            amount (int): The amount of damage received.
        """
        self._hp -= amount
        self._hp = max(self._hp, 0)

    def heal(self, amount: int) -> None:
        """ 
        Restore the character`s HP by the given amount.
        
        HP cannot exceed the character`s maximum HP.
        
        Args:
           amount (int): The amount of HP restored
        """
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    @property
    def is_alive(self) -> bool:
        """
        Check whether the character is alive.
        
        Returns:
            bool: True if HP is grater than Zero, otherwise False.
        """
        return self.hp > 0


    def attack(self, target) -> None:
        """Attack the target using weapon damage or base damage"""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage

        target.take_damage(damage)
        

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp