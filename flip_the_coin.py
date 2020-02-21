import random, time
print("Flip the coin")
while True:
    outcome=random.randint(1,2)
    if(outcome == 1):
       print("Heads")
    elif(outcome == 2):
       print("Tails")
    time.sleep(1)
