import time

current = time.time()
print("Current time is ", current)
from playsound import playsound


def water(name):
    print(f"Drink your glass of water {name}")
    playsound("D:\\reminder project\water.mp3")
    print("Press Y if you drank otherwise N")
    inp = input()
    if inp == 'Y' or inp == 'y':
        with open("water log.txt", "a") as f:
            f.write(inp)
            localtime = time.asctime()
            print(f"{name} drinks water at {localtime}")
    elif inp == 'N' or inp == 'n':
        with open("water log.txt", "a") as fk:
            localtime = time.asctime()
            fk.write(f"\nSkipped drink at {localtime}")
    time.sleep(3)
    print()


def eyes(name):
    print(f"Give rest to your eyes for some minutes..")
    playsound("D:\\reminder project\old.mp3")
    print("Please type \"Done\" if completed otherwise \"No\" ")
    in1 = input()
    if in1 == "Done" or in1 == "done":
        with open("eyes log.txt", "a") as f:
            f.write(in1)
            localtime = time.asctime()
            print(f"{name} eases his/her eyes at {localtime}")

    elif in1 == 'No' or in1 == 'no':
        with open("eyes log.txt", "a") as fk:
            localtime = time.asctime()
            fk.write(f"\nSkipped eyes at {localtime}")
    time.sleep(5)
    print()


def exercise(name):
    print(f"Do some exercise {name} bro")
    playsound("D:\\reminder project\\bomb.mp3")
    print("Please type \"Done\" if completed otherwise \"No\" ")
    in1 = input()
    if in1 == "Done" or in1 == "done":
        with open("exercise log.txt", "a") as f:
            f.write(in1)
            localtime = time.asctime()
            print(f"{name} does his/her exercise at {localtime}")

    elif in1 == 'No' or in1 == 'no':
        with open("eyes log.txt", "a") as fk:
            localtime = time.asctime()
            fk.write(f"\nSkipped exercise at {localtime}")
    time.sleep(4)
    print()


# --------------------------------------------------------------------------------------------------
name = input("What's your name buddy ?")
print(f"welcome {name} to the REMINDER PROGRAM for being a Healthy programmer. Hope you like it.")
for i in range(0, 2):
    water(name)
    print()
    for j in range(i, i + 1):
        eyes(name)
        print()
        for k in range(i, i + 1):
            print()
            exercise(name)
for i in range(0, 2):
    water(name)
    print()
    for j in range(i, i + 1):
        print()
        eyes(name)
for l in range(0, 1):
    print()
    water(name)

print("Please provide us your feedback by just commenting here !")
with open("feeedback.txt", "a") as l:
    l.write(input())