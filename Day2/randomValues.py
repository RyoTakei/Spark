import random

print(dir(random))

print("random.randint(0, 10)")
for i in range(0, 10):
    print(random.randint(0, 10))

###########################

print("\nradom.random()")
for i in range(0, 10):
    print(random.random())

###########################

print("\nrandom.uniform(0.0, 15.5)")
for i in range(0, 10):
    print(random.uniform(0.0, 15.5))

##########################

print("\nrandom.randrange(10)")
for i in range(0, 10):
    print(random.randrange(10))

##########################

print("\nrandom.randrange(10, 20, 2)")
for i in range(0, 10):
    print(random.randrange(10, 20, 2))

##########################

print("\nrandom.choice(['Annika', 'Anika', 'Ryo', 'Micah', 'Solomon']")
for i in range(0, 10):
    print(random.choice(["Annika", "Anika", "Ryo", "Micah", "Solomon"]))

#########################

words = "2898 is the best".split()
print("\n", words)
for i in range(0, 10):
    random.shuffle(words)
    print(words)


words2 = "1510 is something bad trash hahahhaa".split()
for i in range(0, 10):
    random.shuffle(words2)
    print(words2)
