import math

import gun


class TTKCalculator:
    def __init__(self, weapon: gun.Gun, vitality: float, bullet_res: float,
                 headshot: bool, plate_type: str):
        self.weapon = weapon
        self.vitality = vitality
        self.bullet_res = bullet_res
        self.headshot = headshot
        self.plate_type = plate_type

    def bullet_damage_at_distance(self, distance: float):
        base_damage = self.weapon.c_dmg
        if self.weapon.c_range < distance < self.weapon.l_range:
            a = (self.weapon.l_dmg - self.weapon.c_dmg) / (self.weapon.l_range - self.weapon.c_range)
            b = self.weapon.c_dmg - self.weapon.c_range * a
            base_damage = a * distance + b

        if distance >= self.weapon.l_range:
            base_damage = self.weapon.l_dmg

        if self.headshot:
            return base_damage * self.weapon.hs_multi

        if self.plate_type == "none":
            p_multi = 1
        elif self.plate_type == "steel":
            p_multi = 0.9
        elif self.plate_type == "composite":
            p_multi = 0.8
        else:
            p_multi = 0.2

        return base_damage * p_multi

    def bullets_needed_to_kill(self, distance: float):
        return math.ceil(((100 + self.bullet_res * (1 - self.weapon.armorpen))
                          * self.vitality / 100) / self.bullet_damage_at_distance(distance))

    def ttk(self, distance):
        return (60 * (self.bullets_needed_to_kill(distance) - 1)) / self.weapon.firerate
