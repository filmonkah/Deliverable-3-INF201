from Character import Character


class Battle: 
    """Manages turn-based combat between two characters"""

    MAX_ROUNDS: int = 1000 #stops the battle if no one can win 

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        initialise the Battle 

        Args: 
            hero: the character that attacks first in evry round 
            enemy: the character that attacks second in every round 
        """
        self.hero = hero # attacks first 
        self.enemy = enemy # attacks second, if still alive 
        self.round_number = 0 # number of rounds played so far 
        self.log:  list[str] = [] # one line of text per round

    def play_round(self) -> str:
        """
        play one round: the hero attcks the enemy, and if the enemy is still alive, the enemy attacks back 

        Returns: 
            A text describing the HP og both characters after the round 
        """
        self.round_number += 1 #count the new round 
        self.hero.attack(self.enemy) #hero always attacks first 
        if self.enemy.is_alive: # a dead enemy cannot attack 
            self.enemy.attack(self.hero) #enemy attacks back 

        return (
            f"Round {self.round_number}: "
            f"{self.hero.name} {self.hero.hp} HP, {self.enemy.name} {self.enemy.hp} HP"
        )

    def simulate_battle(self) -> Character | None: 
        """
        Play rouunds until one of the Characters is no longer alive. 

        Each round is saved as a line of text iin self.log 

        Returns: 
            The winner, or None if no one won within MAX_ROUNDS rounds 
        """
        while self.hero.is_alive and self.enemy.is_alive: #keep going while both are alive 
            if self.round_number >= self.MAX_ROUNDS: # safety stop to avoid an endless loop 
                return None #no winner 
            self.log.append(self.play_round()) #play a round and save the text 

        if self.hero.is_alive: #the enemy died first 
            return self.hero
        return self.enemy #otherwise the enemy is the winner 
    
