from typing import Tuple

"""
    vvvv      YOUR SOLUTION      vvvv
"""


class Entity:

    def __init__(self, name: str, coords: Tuple[int, int], hit_points: int) -> None:
        # "constructor", more precisely "initializer"
        # initialize Entity here
        # name is string such as "Rob"
        # coords is tuple to represent x and y coordinates in the field: (1, 2) menas x = 1 and y = 2; expect also negative values
        # hitpoints represents count of remaining hitpoints as int, 0 or less hitpoints means death
        self.name = name 
        self.coords= coords
        self.hit_points = hit_points


    def take_damage(self, damage_amount: int) -> None:
        # m# method to apply damage on this entity, it takes damage_amount and applies it by own rules to the entity
        # this is abstract method, just keep it as it is
        raise NotImplementedError("This method is abstract. Please implement it")  # in the child, not here :-)

    def is_alive(self) -> bool:
        # method to check if entity is alive
        # return True if it has hit points above 0
        # return False if it has hit points equal to 0 or less
        # return True if self.hit_points > 0 else
        if self.hit_points > 0:
            return True
        else:
            return False
                
    def get_distance(self, other_coords: Tuple[int, int]) -> int:
        # method to count distance to other object
        # for calculation of distance use Taxicab/Manhattan metric: https://en.wikipedia.org/wiki/Taxicab_geometry
        # returns the distance
        x1, y1 = self.coords
        x2, y2 = other_coords
        return abs(x1 - x2) + abs(y1 - y2)


class Rock(Entity):

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # rock takes damage only when it is hit with damage_amount of at least 10,
        if damage_amount >= 10:
            # each such hit takes him 1 hitpoint, smaller hits don't cause any damage to him
            self.hit_points -= 1
        

class Furniture(Entity):
    # add take_damage method as for the Rock
    # Furniture takes as damage the whole amount of damage_amount incoming
    def take_damage(self, damage_amount: int) -> int:
        self.hit_points = self.hit_points - damage_amount


class LivingEntity(Entity):

    def __init__(self, name: str, coords: Tuple[int, int], hit_points: int, level: int, damage: int, attack_range: int) -> None:
        # "constructor", more precisely "initializer"
        # use parent constructor
        super().__init__(name, coords, hit_points)
        # initialize level, damage and attack_range after both are ints
        self.level = level
        self.damage = damage
        self.attack_range = attack_range
        
        

    def level_up(self) -> None:
        # this method should increase the level of this entity by 1
        self.level += 1

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # the whole damage_amount is applied to hitpoints
        self.hit_points = self.hit_points - damage_amount

    def hit(self, other_entity: Entity) -> None:
        # method to hit other entity to cause them to take damage
        # this is abstract method, just keep it as it is
        raise NotImplementedError("This method is abstract. Please implement it")  # in the child, not here :-)

    def move(self, vector: Tuple[int, int]) -> None:
        # method to make entity move on the board
        # it expects vector of steps in x and y directions, the vector is represented as tuple (x, y)
        # the move is executed by editing coordinates by the vector elements
        # x is editing x axis and y is editing y axis
        # +x, -x, +y, -y define also direction of move
        current_coord_x, current_coord_y = self.coords
        next_coord_x, next_coord_y = vector
        move_x = current_coord_x + next_coord_x
        move_y = current_coord_y + next_coord_y
        self.coords = (move_x, move_y)


    def in_range(self, other_entity: Entity) -> bool:
        # method to check if other entity is in range
        if self.get_distance(other_entity.coords) <= self.attack_range:
            # return True if get_distance to other entity <= self.range
            return True
        else: 
            # return False if get_distance to other entity > self.range
            return False



class Warrior(LivingEntity):

    def hit(self, other_entity: Entity) -> None:
        #  implement hit to another entity
        #  if other entity is in range make it to take damage with it's own method take_damage
        if super().in_range(other_entity):
        #   damage_amount applied to other entity is equal to damage of attacking entity
            other_entity.take_damage(self.damage)
        

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # Warrior is taking damage only when the damage_amount is bigger then his level
        if damage_amount > self.level:
            self.hit_points = self.damage - self.hit_points 
        #   If damage is bigger than level Warrior takes the difference as a damage_amount
        #   Else Warrior takes no damage
        # else:
        #     self.hit_points 
        

    def level_up(self) -> None:
        # this method should increase the level according to parent; use call to parent's method
        # also increase damage by 1 and hit_points by 2
        super().level_up()
        self.damage += 1
        self.hit_points += 2


class Archer(LivingEntity):

    def hit(self, other_entity: Entity) -> None:
        # implement hit to another entity
        #   if other entity is in range make it to take damage with it's own method take_damage
        if super().in_range(other_entity):
        #       damage_amount applied to other entity is equal to damage of attacking entity
            other_entity.take_damage(self.damage)

    def level_up(self) -> None:
        # this method should increase the level according to parent; use call to parent's method
        # also increase damage by 2 and hit_points by 1
        super().level_up()
        self.damage += 2
        self.hit_points += 1


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


# Simple Entity tests
entity = Entity("E", (0, 0), 10)
# constructor
assert entity.name == "E"
assert entity.coords == (0, 0)
assert entity.hit_points == 10
# is alive check
assert entity.is_alive()
# get distance check
assert entity.get_distance((0, 0)) == 0

# Rock tests
rocky = Rock("Rocky", (0, 1), 5)
# # constructor
assert rocky.name == "Rocky"
assert rocky.coords == (0, 1)
assert rocky.hit_points == 5
# # is alive check
assert rocky.is_alive()
# # get distance check
assert rocky.get_distance((0, 0)) == 1
# # damage taking
rocky.take_damage(7)
assert rocky.hit_points == 5
rocky.take_damage(100)
assert rocky.hit_points == 4

# Table tests
table = Furniture("Table", (1, 0), 3)
# constructor
assert table.name == "Table"
assert table.coords == (1, 0)
assert table.hit_points == 3

# is alive check
assert table.is_alive()
# get distance check
assert table.get_distance((0, 0)) == 1
# damage taking
table.take_damage(2)
assert table.hit_points == 1
table.take_damage(2)
assert table.hit_points == -1
assert not table.is_alive()

# LivingEntity tests
tim = LivingEntity("Tim", (-1, 0), 3, 1, 1, 1)
# constructor
assert tim.name == "Tim"
assert tim.coords == (-1, 0)
assert tim.hit_points == 3
assert tim.level == 1
assert tim.damage == 1
assert tim.attack_range == 1
# is alive check
assert tim.is_alive()
# get distance check
assert tim.get_distance((0, 0)) == 1
# level up check
tim.level_up()
assert tim.level == 2
# damage taking
tim.take_damage(1)
assert tim.hit_points == 2
assert tim.is_alive()
# move check
assert tim.in_range(entity)
tim.move((0, -1))
assert not tim.in_range(entity)

# # Warrior tests
willy = Warrior("William Wallace", (1, 1), 3, 5, 8, 2)
# # constructor
assert willy.name == "William Wallace"
assert willy.coords == (1, 1)
assert willy.hit_points == 3
assert willy.level == 5
assert willy.damage == 8
assert willy.attack_range == 2
# # is alive check
assert willy.is_alive()
# # get distance check
assert willy.get_distance((0, 0)) == 2
# # level up check
willy.level_up()
assert willy.hit_points == 5
assert willy.level == 6
assert willy.damage == 9
# # damage taking
willy.take_damage(1)
assert willy.hit_points == 5
willy.take_damage(7)
assert willy.hit_points == 4
# # fight checks
rocky = Rock("Rocky", (0, 1), 5)
willy.hit(rocky)
assert rocky.hit_points == 5
table = Furniture("Table", (1, 0), 3)
willy.hit(table)
assert table.hit_points == -6
tim = LivingEntity("Tim", (-1, 0), 3, 1, 1, 1)
willy.hit(tim)
assert tim.hit_points == 3
willy.move((-1, -1))
assert willy.get_distance((0, 0)) == 0
willy.hit(tim)
assert tim.hit_points == -6

# Archer tests
rob = Archer("Robin Hood", (5, 8), 3, 1, 7, 10)
# constructor
assert rob.name == "Robin Hood"
assert rob.coords == (5, 8)
assert rob.hit_points == 3
assert rob.level == 1
assert rob.damage == 7
assert rob.attack_range == 10
# is alive check
assert rob.is_alive()
# get distance check
assert rob.get_distance((0, 0)) == 13
# level up check
rob.level_up()
assert rob.hit_points == 4
assert rob.level == 2
assert rob.damage == 9
# damage taking
rob.take_damage(1)
assert rob.hit_points == 3
# fight checks
willy = Warrior(
    name="William Wallace", 
    coords=(1, 1), 
    hit_points=3, 
    level=5, 
    damage=8, 
    attack_range=2)
rob.hit(willy)
assert willy.hit_points == 3
rob.move((0, -1))
rob.hit(willy)
assert willy.hit_points == 5    #main TC this value was -1
assert willy.is_alive()