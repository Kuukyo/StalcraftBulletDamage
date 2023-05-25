from src import lib
import math


class Gun:
    def __init__(self, name: str):
        weapons = lib.load_mem("../resources/guns.json")
        gun_stats = weapons[name]

        self.c_dmg = gun_stats["c_dmg"]
        self.l_dmg = gun_stats["l_dmg"]
        self.c_range = gun_stats["c_range"]
        self.l_range = gun_stats["l_range"]
        self.max_range = gun_stats["max_range"]
        self.firerate = gun_stats["firerate"]
        self.armorpen = gun_stats["armorpen"]
        self.hs_multi = gun_stats["hs_multi"]
        self.spread = gun_stats["spread"]

    def c_dps(self):
        return self.c_dmg * self.firerate / 60

    def l_dps(self):
        return self.l_dmg * self.firerate / 60

    def accurate_range(self):
        return 0.25 / (math.tan(math.degrees(self.spread) / 2))