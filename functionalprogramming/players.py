players=[
    {"name":"sachin","matches":500,"rank":1},
    {"name":"dravid","matches":450,"rank":12},
    {"name":"sehwag","matches":250,"rank":52},
    {"name":"msd","matches":360,"rank":7},
]

# print(list(map(lambda dict:dict["name"],players)))

# print(list(map(lambda dict:dict["rank"],players)))

play=list(filter(lambda dict:dict["matches"]>320,players))
names=list(map(lambda player:player["name"],play))
print(names)