from cgi import print_directory
from sqlite3 import DateFromTicks


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

bad_foods = ['pineapple', 'dates', 'bludwurst']
food = 'fried chickn'

if food not in bad_foods:
    print(f"\n{food.title()}")
    print("\nThis some good shiz.")
if food != 'pineapple':
    print('\nShieeeeeet')
if 'pineapple' in bad_foods:
    print("\nDag, that sucks.")
if 'bludwurst' in bad_foods:
    print(f"\n{food.title()} > Bludwurst")

if food != "fried chickn":
    print(f"\nThis {food} is way better than some bullshit dates.")

if food == "dates":
    print(f"\nThis {food} is fuckin awful.")