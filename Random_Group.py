from itertools import count
import random
import time
number_of_member = int(input("number_of_member:"))
list = []
number_of_member_in_group = int(input("Number of member in group:"))
for i in range(number_of_member):
    names = str(input("Enter names of members:"))
    list.append(names)
team=[]
for i in range(len(list)):
    team.append(list[random.randint(0,len(list)-1)])
    for j in team:
        if team.count(j)>1:
            team.remove(j)
    for x in list:
        if x not in team:
            team.append(x)
new_team = []
for member in range(int(len(list)/number_of_member_in_group)):
    new_team.append([])
    for i in range(number_of_member_in_group*member,number_of_member_in_group*member+number_of_member_in_group):
        new_team[member].append(team[i])
if (number_of_member//number_of_member_in_group) == (number_of_member/number_of_member_in_group):
    for y in range(len(new_team)):
        print(y+1,":",new_team[y])
else:
    for v in range(number_of_member_in_group):
        team.append("Nobody")
        if len(team)%number_of_member_in_group == 0:
            break
    new_team1 = []
    for member_x in range(int(len(team)/number_of_member_in_group)):
        new_team1.append([])
        for y_x in range(number_of_member_in_group*member_x,number_of_member_in_group*member_x+number_of_member_in_group):
            new_team1[member_x].append(team[y_x])
    for x_z in range(len(new_team1)):
        print(x_z+1,":",new_team1[x_z])
    
    



    

