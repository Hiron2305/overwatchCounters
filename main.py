roles = {"Tank": ["Roadhog", "Wrecking Ball", "D.Va", "Winston", "Sigma", "Orisa", "Zarya", "Reinhardt"],
         "DD": ["Hanzo", "Cassidy", "Reaper", "Echo", "Ashe", "Genji", "Widowmaker", "Doomfist",
                "Tracer", "Solider_76", "Junkrat", "Mei", "Pharah", "Torbjorn", "Sombra", "Symmetra", "Bastion"],
         "Healer": ["Moira", "Baptiste", "Lucio", "Mercy", "Ana", "Zenyatta", "Brigitte"]}
print("List of character: ")
for key, value in roles.items():
    print(key, ':', value)

first_tank = input("First tank: ")
second_tank = input("Second tank: ")
first_dd = input("First damage dealer: ")
second_dd = input("Second damage dealer:  ")
first_healer = input("First healer: ")
second_healer = input("Second healer: ")

# "": ["","",""],
first_enemy = {"Bastion": ["Genji", "Widowmaker", "Hanzo"],
               "D.Va": ["Mei", "Junkrat", "Reaper"],
               "Genji": ["Mei", "Winston", "Zarya"],
               "Hanzo": ["Genji", "Tracer", "Winston"],
               "Mercy": ["Tracer", "Genji", "Roadhog"],
               "Junkrat": ["Pharah", "Widowmaker", "Solider_76"],
               "Lucio": ["Mei", "Pharah", "Cassidy"],
               "Cassidy": ["Widowmaker", "Genji", "Pharah"],
               "Mei": ["Pharah", "Reaper", "Widowmaker"],
               "Pharah": ["Solider_76", "Roadhog", "Torbjorn"],
               "Reaper": ["Cassidy", "Pharah", "Genji"],
               "Reinhardt": ["Mei", "Bastion", "Junkrat"],
               "Roadhog": ["Reaper", "Mei", "D.Va"],
               "Solider_76": ["Genji", "Roadhog", "Cassidy"],
               "Symmetra": ["Pharah", "Roadhog", "Winston"],
               "Torbjorn": ["Widowmaker", "Hanzo", "Junkrat"],
               "Tracer": ["Cassidy", "Roadhog", "Pharah"],
               "Widowmaker": ["Genji", "D.Va", "Winston"],
               "Zarya": ["Pharah", "Reaper", "Mei"],
               "Zenyatta": ["Widowmaker", "Reaper", "Genji"]}

res_roles = {"Tank": [],
             "DD": [],
             "Healer": []}
res_list = list()
Team = list()
f_tank_counters = first_enemy[first_tank]
s_tank_counters = first_enemy[second_tank]
f_dd_counters = first_enemy[first_dd]
s_dd_counters = first_enemy[second_dd]
f_heal_counters = first_enemy[first_healer]
s_heal_counters = first_enemy[second_healer]
res_list.extend(
    [*f_tank_counters, *s_tank_counters, *f_dd_counters, *s_dd_counters, *f_heal_counters, *s_heal_counters])

for i in res_list:
    if i in roles["Tank"]:
        Tank_counter = res_list.count(i)
        for T in range(Tank_counter):
            res_list.remove(i)
        res_roles["Tank"].append([i, Tank_counter])

    if i in roles["DD"]:
        DD_counter = res_list.count(i)
        for D in range(DD_counter):
            res_list.remove(i)
        res_roles["DD"].append([i, DD_counter])

    if i in roles["Healer"]:
        Healer_counter = res_list.count(i)
        for H in range(Healer_counter):
            res_list.remove(i)
        res_roles["Healer"].append([i, Healer_counter])

list_for_max_DD = list()
list_for_max_Healer = list()
list_for_max_Tank = list()

for T_count in res_roles["Tank"]:
    list_for_max_Tank.append(T_count[1])
if len(list_for_max_Tank) >= 2:
    for T_true_ret in res_roles["Tank"]:
        if T_true_ret[1] == max(list_for_max_Tank):
            print("Tank: ", T_true_ret[0])
            list_for_max_Tank.remove(max(list_for_max_Tank))
else:
    for T_true_ret in res_roles["Tank"]:
        print("Tank: ", T_true_ret[0], "+ Everyone")

for DD_count in res_roles["DD"]:
    list_for_max_DD.append(DD_count[1])
if len(list_for_max_DD) >= 2:
    for D_true_ret in res_roles["DD"]:
        if D_true_ret[1] == max(list_for_max_DD):
            print(D_true_ret[0])
            list_for_max_DD.remove(max(list_for_max_DD))
else:
    for D_true_ret in res_roles["DD"]:
        print(D_true_ret[0], "+ Everyone")

for H_count in res_roles["Healer"]:
    list_for_max_Healer.append(H_count[1])
if len(list_for_max_Healer) >= 2:
            for H_true_ret in res_roles["Healer"]:
                if H_true_ret[1] == max(list_for_max_Healer):
                    print(H_true_ret[0])
                    list_for_max_Healer.remove(max(list_for_max_Healer))
else:
    for H_true_ret in res_roles["Healer"]:
        print(H_true_ret[0], "+ Everyone")

print(res_roles)