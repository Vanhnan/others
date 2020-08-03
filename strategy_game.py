from soldiers_heroes import *
import random

hero1 = Hero(1, "light")
hero2 = Hero(2, "dark")

teams = ["light", "dark"]
soldiers = [Soldier(i, random.choice(teams)) for i in range(10)]

dark_team = []
light_team = []
for i in soldiers:
    if i.team=="dark":
        dark_team.append(i)
    else:
        light_team.append(i)


for i in range(len(dark_team)):
    if hero1.team=="dark":
        hero1.level_up()
    if hero2.team=="dark":
        hero2.level_up()

for i in range(len(light_team)):
    if hero1.team=="light":
        hero1.level_up()
    if hero2.team=="light":
        hero2.level_up()

##print("dark team members => "+str(len(dark_team)))
##print("light team members => "+str(len(light_team)))
##print(hero1.team, hero1.lvl)
##print(hero2.team, hero2.lvl)

light_team[0].follow_hero(hero1)
