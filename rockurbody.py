import sys
from time import sleep

lines = [
        ("I wanna da-", 1.25),
("I wanna dance in the lights", 2.5),
("I wanna ro-", 1),
("I wanna rock your body", 2.75),
("I wanna go", 1.25),
("I wanna go for a ride", 3),
("Hop in the music and", 1.5),
("Rock your body", 1.75),
("Rock that body", 1),
("come on, come on", 1),
("Rock that body", 1),
("(Rock your body)", 1),
("Rock that body", 1),
("come on, come on", 1),
("Rock that body", 2.5),
    ]
def printLyrics(): lines

for line, duration in lines:
    print(line)
    sleep (duration)
    
printLyrics()