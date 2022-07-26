import pandas as pd

first_tank = input("First tank: ")
second_tank = input("Second tank: ")
first_dd = input("First damage dealer: ")
second_dd = input("Second damage dealer:  ")
first_healer = input("First healer: ")
second_healer = input("Second healer: ")

first_enemy = {"Bastion": ["Genji", "Widowmaker", "Hanzo"],
               "D.Va": ["Mei", "Junkrat", "Reaper"],
               "Genji": ["Mei", "Winston", "Zarya"]}

roles = {"Tank": ["Roadhog","Wrecking Ball","D.Va","Winston","Sigma","Orisa","Zarya","Reinhardt"],
         "DD": ["Hanzo","Cassidy","Reaper","Echo","Ashe","Genji","Widowmaker","Doomfist","Tracer","Solider_76","Junkrat","Mei","Pharah","Torbjorn","Sombra","Symmetra","Bastion"],
         "Healer": ["Moira","Baptiste","Lucio","Mercy","Ana","Zenyatta","Brigitte"]}
res_roles = {"Tank": [],
             "DD": [],
             "Healer": []}

res_list = list()

f_tank_counters = first_enemy[first_tank]
s_tank_counters = first_enemy[second_tank]
f_dd_counters = first_enemy[first_dd]
s_dd_counters = first_enemy[second_dd]
f_heal_counters = first_enemy[first_healer]
s_heal_counters = first_enemy[second_healer]
res_list.extend([*f_tank_counters,*s_tank_counters,*f_dd_counters,*s_dd_counters,*f_heal_counters,*s_heal_counters])


for i in res_list:
    if i in roles["Tank"]:
        Tank_counter = res_list.count(i)
        res_roles["Tank"] = {i: Tank_counter}

    if i in roles["DD"]:
        DD_counter = res_list.count(i)
        res_roles["DD"] = {i: DD_counter}

    if i in roles["Healer"]:
        res_roles["Healer"].append(i)
print(res_roles)