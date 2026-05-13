from abc import ABC, abstractmethod

class Spell(ABC):

    def __init__(self, name: str, damage: int, mana_cost: int) -> None:
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self) -> int:
        pass

class Fireball(Spell):
    def __init__(self) -> None:
        super().__init__("Fireball", 35, 15)

    def cast(self) -> int:
        return self.damage

class IceLance(Spell):
    def __init__(self) -> None:
        super().__init__("Ice Lance", 25, 10)

    def cast(self) -> int:
        return self.damage

class LightningBolt(Spell):
    def __init__(self) -> None:
        super().__init__("Lightning Bolt", 40, 20)

    def cast(self) -> int:
        return self.damage

class Unit(ABC):

    def __init__(self, strength: int, dexterity: int, constitution: int,
                 wisdom: int, intelligence: int, charisma: int) -> None:

        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

        self.spells = []
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self) -> int:
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        pass

    def add_spell(self, spell: Spell) -> None:
        self.spells.append(spell)

    def cast_spell(self, index: int) -> int:
        spell = self.spells[index]

        if self.mana < spell.mana_cost:
            raise ValueError("Недостаточно маны")

        self.mana -= spell.mana_cost
        return spell.cast()

class Character(Unit):

    AVAILABLE_CLASSES = ("warrior", "mage", "hunter")

    def __init__(
        self,
        strength: int,
        dexterity: int,
        constitution: int,
        wisdom: int,
        intelligence: int,
        charisma: int,
        character_class: str
    ) -> None:

        super().__init__(
            strength,
            dexterity,
            constitution,
            wisdom,
            intelligence,
            charisma
        )

        if character_class not in self.AVAILABLE_CLASSES:
            raise ValueError("Invalid class")

        self.character_class = character_class

        self.max_health = self.calculate_max_health()
        self.health = self.max_health

        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana

    def calculate_max_health(self) -> int:
        return int(self.constitution * 10 + self.strength / 2)

    def calculate_damage(self) -> int:

        if self.character_class == "warrior":
            return int(self.strength * 2.2 + self.constitution / 3)

        if self.character_class == "mage":
            return int(self.intelligence * 2.5 + self.wisdom / 2)

        if self.character_class == "hunter":
            return int(self.dexterity * 1.9 + self.strength / 3)

        return 0

    def calculate_defense(self) -> int:

        if self.character_class == "warrior":
            return int(self.constitution * 1.8 + self.strength / 4)

        if self.character_class == "mage":
            return int(self.wisdom * 1.3 + self.intelligence / 6)

        if self.character_class == "hunter":
            return int(self.dexterity * 1.6 + self.constitution / 5)

        return 0

    def calculate_max_mana(self) -> int:

        if self.character_class == "warrior":
            return int(self.intelligence + self.strength / 2)

        if self.character_class == "mage":
            return int(self.intelligence * 3 + self.wisdom)

        if self.character_class == "hunter":
            return int(self.dexterity * 1.5 + self.wisdom / 2)

        return 0