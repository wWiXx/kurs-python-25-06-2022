"""
a = "a"
b = 10

print("{:^30} {:<6.2f}".format("a", 10))

print(f"{a:^30} {b}")
"""

tomato = "pomidor"
tomatosCalories = 19
tomatosProteins = 1
tomatosFat = 0
tomatosCarbo = 4
tomatosPricePerKilo = 5.7

mozzarella = "ser mozzarella"
mozzarellaCalories = 248
mozzarellaProteins = 18
mozzarellaFat = 19
mozzarellaCarbo = 2
mozzarellaPricePerKilo = 38.32

salad = "sałata"
saladCalories = 13
saladProteins = 1
saladFat = 0
saladCarbo = 2
saladPricePerKilo = 3.15



tomatoScaler = 3.5
tomatoCountedCalories = round(tomatoScaler * tomatosCalories,2)
tomatoCountedProteins = round(tomatoScaler * tomatosProteins,2)
tomatoCountedFat = round(tomatoScaler * tomatosFat,2)
tomatoCountedCarbo = round(tomatoScaler * tomatosCarbo,2)
tomatoCountedPrice = round(0.350 * tomatosPricePerKilo,2)



mozzarellaScaler = 3.25
mozzarelaCountedCalories = round(mozzarellaScaler * mozzarellaCalories,2)
mozzarellaCountedProteins = round(mozzarellaScaler * mozzarellaProteins,2)
mozzarelaCountedFat = round(mozzarellaScaler * mozzarellaFat,2)
mozzarellaCountedCarbo = round(mozzarellaScaler * mozzarellaCarbo,2)
mozzarellaCountedPrice = 0.325 * mozzarellaPricePerKilo



saladScaler = 3.5
saladCountedCalories = saladScaler * saladCalories
saladCountedProteins = saladScaler * saladProteins
saladCountedFat = saladScaler * saladFat
saladCountedCarbo = saladScaler * saladCarbo
saladCountedPrice = 0.350 * saladPricePerKilo




print(f"{tomato:<15}, kalorie:{tomatoCountedCalories:6.2f}, b: {tomatoCountedProteins:5.2f}, t: {tomatoCountedFat:5.2f}, w: {tomatoCountedCarbo:5.2f}, waga: {'350 g':4}, koszt: {str(tomatoCountedPrice)+' PLN'}")
print(f"{mozzarella:<15}, kalorie:{tomatoCountedCalories:6.2f}, b: {tomatoCountedProteins:5.2f}, t: {tomatoCountedFat:5.2f}, w: {tomatoCountedCarbo:5.2f}, waga: {'350 g':4}, koszt: {str(tomatoCountedPrice)+' PLN'}")
print(f"{tomato:<15}, kalorie:{tomatoCountedCalories:6.2f}, b: {tomatoCountedProteins:5.2f}, t: {tomatoCountedFat:5.2f}, w: {tomatoCountedCarbo:5.2f}, waga: {'350 g':4}, koszt: {str(tomatoCountedPrice)+' PLN'}")
#print("{:15},{text:}{:6.2f}".format(tomato,tomatoCountedCalories))