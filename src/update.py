import lib
import os
from jsonpath_ng.ext import parse


def convert(item):
    if item == "7.62":
        return 0.175
    if item == "5.45":
        return 0.1
    if item == "5.56":
        return 0.1
    if item == "9x39":
        return 0.2
    if item == "12.7":
        return 0.25
    if item == "12 caliber":
        return 0.2
    if item == "9 mm":
        return 0.05


guns = {}

exclude = ["device", "heavy", "melee", "_variants"]
for root, dirs, files in os.walk("../resources/stalcraft-database/global/items/weapon"):
    dirs[:] = [d for d in dirs if d not in exclude]

    for file in files:
        if file.endswith(".json") and file != "_variants":
            gun = lib.load_mem(f"{root}/{file}")
            gun_name = gun["name"]["lines"]["en"]
            print(gun_name)
            guns[gun_name] = {}
            guns[gun_name]["c_dmg"] = parse("$.infoBlocks[?(@.type=='damage')].startDamage").find(gun)[0].value * 1.25
            guns[gun_name]["l_dmg"] = parse("$.infoBlocks[?(@.type=='damage')].endDamage").find(gun)[0].value * 1.25
            guns[gun_name]["c_range"] = parse("$.infoBlocks[?(@.type=='damage')].damageDecreaseStart").find(gun)[0].value
            guns[gun_name]["l_range"] = parse("$.infoBlocks[?(@.type=='damage')].damageDecreaseEnd").find(gun)[0].value
            guns[gun_name]["max_range"] = parse("$.infoBlocks[?(@.type=='damage')].maxDistance").find(gun)[0].value
            guns[gun_name]["firerate"] = parse("$.infoBlocks[?(@.type == 'list')].elements[?(@.type == 'numeric' & @.name.lines.en == 'Rate of fire')].value").find(gun)[0].value
            guns[gun_name]["armorpen"] = convert(parse("$.infoBlocks[?(@.type == 'list')].elements[?(@.type == 'key-value' & @.key.lines.en == 'Ammo type')].value.lines.en").find(gun)[0].value)
            guns[gun_name]["hs_multi"] = float(parse("$.infoBlocks[?(@.type == 'list')].elements[?(@.type == 'text' & @.text.key == 'weapon.tooltip.weapon.head_damage_modifier')].text.args.modifier").find(gun)[0].value)
            guns[gun_name]["spread"] = parse("$.infoBlocks[?(@.type == 'list')].elements[?(@.type == 'numeric' & @.name.lines.en=='Spread')].value").find(gun)[0].value
            guns[gun_name]["v_recoil"] = parse("$.infoBlocks[?(@.type == 'list')].elements[?(@.type == 'numeric' & @.name.lines.en=='Vertical recoil')].value").find(gun)[0].value
            guns[gun_name]["h_recoil"] = parse("$.infoBlocks[?(@.type == 'list')].elements[?(@.type == 'numeric' & @.name.lines.en=='Horizontal recoil')].value").find(gun)[0].value

lib.dump_mem(guns, "../resources/guns.json")
