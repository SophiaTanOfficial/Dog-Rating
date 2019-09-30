from random import randint
# 1. Write a function called basic_rating that takes in a dog's name and returns a string that says "_____ is a cute dog. ___/10"
#    For example, basic_rating("Spot") could return "Spot is a cute dog. 10/10"

def basic_rating(dogName):
    return dogName + " is the best! " + str(randint(1, 10)) + "/10"

print (basic_rating("Nunu"))


# 2. Write a function called special_rating that takes in a dog's name, returns a better rating if the dog's name is one of your favorite names.

def special_rating(dogName):
    if dogName == "Nunu":
         return "You are the best dog in the world! 100/10"
    else:
        return dogName + " is the best! " + str(randint(1, 10)) + "/10"
        
print (special_rating("Nunu"))



# 3. Write a function called type_rating that takes in a dog's breed, returns a better rating if the dog is one of your favorite types.

def type_rating(breed):
    if breed == "husky" or breed == "shiba inu":
        return "The best there is! 100/10"
    else:
        return breed + " is the best! " + str(randint(1, 10)) + "/10"
print (type_rating("Labrador"))


# 4. Write a function called ultimate_rating that takes in a dog's name and the dog's breed and returns a rating based on those two factors.
#    BONUS 1: If the user doesn't specify the dog's breed, the function should default to assuming the dog's breed is "unknown".
#    BONUS 2: If the dog's name is Apollo the Corgi, give the dog even more bonus points for being FAMOUS.

def ultimate_rating(name, breed = "Unknown"):
    if name == "Apollo" and breed == "Corgi":
        return "100/10"
    else:
        return name + " The " + breed + " is " + str(randint(1,10)) + "/10"

print (ultimate_rating("Goosh"))
        
    