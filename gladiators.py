import random

# def miss_chance():
#     chance = random.randint(1,100)
#     return chance > 10

gl_1 = {"hp": 100, "damage": None, "dodge": 10, "name": "gladiator_1"}
gl_2 = {"hp": 100, "damage": None, "dodge": 10, "name": "gladiator_2"}

def get_hp(atacker:dict, defender:dict):
    if atacker["hp"] > 0:
        dodge = random.randint(0, 100)
        dmg = (atacker["damage"] * (dodge > defender["dodge"]))
        defender["hp"] -= dmg

        if defender["hp"] < 0:
            defender["hp"] = 0

        info_string = f"{atacker['name']} hit: {dmg} --> {defender['name'] } | {defender['name']}  hp left {defender['hp']} "
        print(info_string)
        return defender["hp"]
    return defender["hp"]

a = [gl_1, gl_2]

while all([gl_1["hp"] > 0, gl_2["hp"] > 0]):
    gl_1["damage"], gl_2["damage"] = random.randint(1, 5), random.randint(1, 5)
    index = random.randint(0,1)
    a[index]["hp"]=get_hp(a[len(a)-1-index], a[index])
    a[len(a)-1-index]["hp"]=get_hp(a[index], a[len(a)-1-index])
    print("_"*10, "\n")


if gl_1["hp"] <= 0 and gl_2["hp"] <= 0:
    print("draw")
elif gl_1["hp"] <= 0:
    print("gladiator_2 win!")
else:
    print("gladiator_1 win!")