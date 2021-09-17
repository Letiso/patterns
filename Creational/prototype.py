from abc import ABC, abstractmethod
import copy
from random import randrange


# Config module


class NPCConfig:
    _races_list = ['orc', 'human', 'high elf']

    _names_dict = {
        'orc': ['Chakub', 'Duffthug', 'Sugbu', 'Gollik', 'Zogstuf', 'Yambul', 'Rok', 'Grimfang'],
        'human': ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Sophia', 'James', 'William'],
        'high elf': ['Durothil', 'Aeson', 'Elora', 'Qildor', 'Sharian', 'Ilyrana', 'Takari', 'Leilatha'],
    }

    _races_stats_dict = {
        'orc': {
            'health': 140,
            'stamina': 150,
            'mana': 80,
        },
        'human': {
            'health': 130,
            'stamina': 120,
            'mana': 120,
        },
        'high elf': {
            'health': 110,
            'stamina': 110,
            'mana': 150,
        }
    }

    _armor_types_dict = {
        'heavy armor': {
            'defence': 45
        },
        'medium armor': {
            'defence': 25,
            'stamina': 50
        },
        'light armor': {
            'defence': 15,
            'mana': 50
        }
    }

    _weapon_types_dict = {
        'warrior': {
            'heavy sword': {
                'damage': 50,
                'ability cost': 30
            },
            'light sword': {
                'damage': 40,
                'ability cost': 20
            },
            'sword and shield': {
                'damage': 30,
                'ability cost': 25,
                'defence': 25
            },
        },
        'mage': {
            'fire_stuff': {
                'damage': 55,
                'ability cost': 30
            },
            'ice_stuff': {
                'damage': 45,
                'ability cost': 20
            },
            'lighting_stuff': {
                'damage': 50,
                'ability cost': 25
            },

        }
    }


# Main module


class NPCPrototype(ABC):
    @abstractmethod
    def clone(self,
              race: str = None,
              name: str = None,
              available_armor: list = None,
              available_weapon: list = None): pass


class NPC(NPCPrototype, NPCConfig):
    def __init__(self):
        self._race = self._name = self._available_armor = self._available_weapon = None
        self._inventory = {
            slot: None for slot in ('armor', 'weapon')
        }
        self._stats = {
            stat: 0 for stat in ('health', 'stamina', 'mana', 'damage', 'ability cost', 'defence')
        }

    def __str__(self):
        return f"\n{'*' * 100}\n" \
               f"Race: {self._race}\n" \
               f"Name: {self._name}\n" \
               f"Class: {self.__class__.__name__}\n" \
               f"{'_' * 25}\n" \
               f"Available equipment: \nArmor   -- {self._available_armor}\nWeapons -- {self._available_weapon}\n" \
               f"{'_' * 25}\n" \
               f"Inventory: \n{self._inventory}\n" \
               f"Stats: \n{self._stats}\n" \
               f"{'*' * 100}\n"

    def _equip_armor(self, armor):
        self._inventory['armor'] = armor
        for stat in NPCConfig._armor_types_dict[armor]:
            self._stats[stat] += NPCConfig._armor_types_dict[armor][stat]

    def _equip_weapon(self, weapon):
        self._inventory['weapon'] = weapon
        for stat in NPCConfig._weapon_types_dict[self.__class__.__name__.lower()][weapon]:
            self._stats[stat] += NPCConfig._weapon_types_dict[self.__class__.__name__.lower()][weapon][stat]

    def _stats_init(self):
        armor = self._available_armor[randrange(len(self._available_armor))]
        weapon = self._available_weapon[randrange(len(self._available_weapon))]

        for stat in NPCConfig._races_stats_dict[self._race]:
            self._stats[stat] += NPCConfig._races_stats_dict[self._race][stat]
        self._equip_armor(armor)
        self._equip_weapon(weapon)

    def clone(self,
              race: str = None,
              name: str = None,
              available_armor: list = None,
              available_weapon: list = None):
        new = copy.deepcopy(self)

        if not race:
            new._race = NPCConfig._races_list[randrange(len(NPCConfig._races_list))]
        else:
            new._race = race

        if not name:
            new._name = NPCConfig._names_dict[new._race][randrange(len(NPCConfig._names_dict[new._race]))]
        else:
            new._name = name

        if available_armor: new._available_armor = available_armor
        if available_weapon: new._available_weapon = available_weapon

        new._stats_init()

        return new


class Warrior(NPC):
    def __init__(self):
        NPC.__init__(self)
        self._stats['stamina'] += 100
        self._available_armor = [armor_type for armor_type in NPCConfig._armor_types_dict
                                 if 'light armor' not in armor_type]
        self._available_weapon = [weapon_type for weapon_type in NPCConfig._weapon_types_dict['warrior']]


class Mage(NPC):
    def __init__(self):
        NPC.__init__(self)
        self._stats['mana'] += 100
        self._available_armor = [armor_type for armor_type in NPCConfig._armor_types_dict
                                 if 'light armor' in armor_type]
        self._available_weapon = [weapon_type for weapon_type in NPCConfig._weapon_types_dict['mage']]


class NPCFactory:
    def __init__(self):
        self._base_warrior = Warrior()
        self._base_mage = Mage()

    def get_random_warrior(self):
        return self._base_warrior.clone()

    def get_random_mage(self):
        return self._base_mage.clone()

    def test(self):
        for npc in self.get_random_warrior(), self.get_random_mage(): print(npc)


if __name__ == '__main__':
    NPCFactory().test()
