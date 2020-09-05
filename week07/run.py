from abc import ABC, abstractmethod
from enum import Enum


class AnimalClass(Enum):
    HERBIVORE = 1
    CARNIVORE = 2
    OMNIVORE = 3


class BodyType(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

    def __ge__(self, other):
        if self.value >= other.value:
            return True
        else:
            return False


class Nature(Enum):
    FEROCIOUS = 1
    DOCILE = 2


class Animal(ABC):

    @abstractmethod
    def __init__(self, animal_class: AnimalClass, body_type: BodyType, nature: Nature):
        assert isinstance(animal_class, (AnimalClass,)) \
               and isinstance(body_type, (BodyType,)) \
               and isinstance(nature, (Nature,))
        self.animal_class = animal_class
        self.body_type = body_type
        self.nature = nature

    def is_ferocious(self):
        if self.body_type >= BodyType.MEDIUM \
                and self.animal_class == AnimalClass.HERBIVORE \
                and self.nature == Nature.FEROCIOUS:
            return True
        else:
            return False

    pass


def is_suitable_as_pet(self):
    if self.is_ferocious():
        return False
    else:
        return True


class TraitPet(Animal):

    def __init__(self, name: str, animal_class: AnimalClass, body_type: BodyType, nature: Nature):
        super().__init__(animal_class, body_type, nature)
        self.name = name

    def is_suitable_as_pet(self):
        return is_suitable_as_pet(self)


class Calls(Enum):
    MEOW = 1
    BARK = 2


class Cat(TraitPet):
    calls = Calls.MEOW


class Dog(TraitPet):
    calls = Calls.BARK


class Zoo:
    def __init__(self, name=None):
        self.name = name
        self.animals = set()
        self.animal_classes = set()

    def __getattr__(self, item):
        if item in self.animal_classes:
            pass
        else:
            super().__getattr__(item)

    def add_animal(self, animal: Animal):
        self.animals.add(animal)
        self.animal_classes.add(animal.__class__.__name__)
        print(len(self.animals))


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    # cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('小花猫 2', AnimalClass.HERBIVORE, BodyType.SMALL, Nature.DOCILE)
    cat3 = Cat('大老虎一号', AnimalClass.HERBIVORE, BodyType.LARGE, Nature.FEROCIOUS)
    print(cat2.is_suitable_as_pet(), cat3.is_suitable_as_pet())
    # 增加一只猫到动物园
    z.add_animal(cat3)
    # 动物园是否有猫这种动物
    print(hasattr(z, 'Cat'))
