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


class Warrior(Character): 
    """Represents a warrior, a defensive character that reduces incoming damage with armor"""

    def __init__(
            self, 
            name: str, 
            hp_max: int = 100,
            damage: int = 10, 
            weapon: Weapon | None = None, 
            armor: int = 5,  
    ) -> None: 
        """
        Inutiakuse the Warrior. 

        Args: 
            name: the name of the warrior 
            hp_max: Max hit points 
            damage: Base damage dealt when the warrior attacks 
            weapon: optional equipped weapon (default = None)
            armor: Amount of damage removed from eacho incoming attacl (default = 5)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor #new attribute only warriors have 

    def take_damage(self, amount: int) -> None: 
        """
        Reduce the incoming damage by armor, then apply it to the warrior`s hp. 
        The reduced damage cannot be negative, so armor never heals the warrior

        Args: 
            amount: The amount of damage before armor is applied
        """
        reduced_amount = max(amount - self.armor, 0) # makes sure that the armor blocks some damage, but never below 0 
        super().take_damage(reduced_amount) #reuse Character.take_damage so HP stays >= 0 

    def __repr__(self) -> str:
        """Representation of warrior object"""
        return f"<Warrior name={self.name} hp={self.hp} damage={self.damage} armor={self.armor}>"


class Mage(Character):
    """Represents a mage, an attacker that uses mana to cast spells with double damage."""

    SPELL_COST: int = 10 # mana needed for one spell 
    MANA_RESTORE: int = 5 #mana restored after a base attack 
    SPELL_MULTIPLIER: int = 2 #Spells deal double damage 

    def __init__(
            self, 
            name: str, 
            hp_max: int = 100, 
            damage: int = 10, 
            weapon: Weapon | None = None, 
            mana: int = 30, 
            mana_max: int = 30,
    ) -> None: 
        """
        Initialise the mage 

        Args: 
            name: The name og the mage 
            hp_max: Max hit points (default = 100)
            damage: Base damage dealt when the mage attacks (default = 10)
            weapon: Optional equipped weapon, only use in base attacks (default = None)
            mana: Mana the mage starts with (default = 30)
            mana_max: Max mana (default = 30)
        """
        super().__init__(name, hp_max, damage, weapon)
        self._mana = min(mana, mana_max)
        self.mana_max = mana_max #upper limit for mana 

    @property
    def mana(self) -> int: 
        """Public read-only property to inspect mana without allowing direct edits"""
        return self._mana

    def attack(self, target: Character) -> None: 
        """
        Attack the target with a spell if there is enough mana, otherwise use a base attack 

        A spell costs 10 mana and deals double base damage, withoutw using any weapon 
        A base attack uses the equipped weapon (if any) and restores 5 mana 

        Args: 
            target: the character that is attacked 
        """
        if self._mana >= self.SPELL_COST: # if enough mana for the spell 
            self._mana -= self.SPELL_COST #pay for the spell 
            target.take_damage(self.damage * self.SPELL_MULTIPLIER) #double damage 
        else: #not enough mana
            super().attack(target) #base attck from Charachter 
            self._mana = min(self._mana + self.MANA_RESTORE, self.mana_max) #restore mana, max mana_max

    def __repr__(self) -> str:
        """Representation of mage object"""
        return f"<Mage name = {self.name} hp={self.hp} damage={self.damage} mana={self.mana}/{self.mana_max}>"