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
tomatoWeight = 350

mozzarellaScaler = 3.25
mozzarelaCountedCalories = round(mozzarellaScaler * mozzarellaCalories,2)
mozzarellaCountedProteins = round(mozzarellaScaler * mozzarellaProteins,2)
mozzarelaCountedFat = round(mozzarellaScaler * mozzarellaFat,2)
mozzarellaCountedCarbo = round(mozzarellaScaler * mozzarellaCarbo,2)
mozzarellaCountedPrice = round(0.325 * mozzarellaPricePerKilo,2)
mozzarellaWeight = 325

saladScaler = 3.5
saladCountedCalories = saladScaler * saladCalories
saladCountedProteins = saladScaler * saladProteins
saladCountedFat = saladScaler * saladFat
saladCountedCarbo = saladScaler * saladCarbo
saladCountedPrice = round(0.350 * saladPricePerKilo,2)
saladWeight = 350

sum = "SUMA"
currency = "PLN"
sumOfCalories = tomatoCountedCalories + mozzarelaCountedCalories + saladCountedCalories
sumOfProteins = tomatoCountedProteins + mozzarellaCountedProteins + saladCountedProteins
sumOfFats = tomatoCountedFat + mozzarelaCountedFat + saladCountedFat
sumOfCarbos = tomatoCountedCarbo + mozzarellaCountedCarbo + saladCountedCarbo
sumOfWeights = tomatoWeight + mozzarellaWeight + saladWeight
sumOfPrices = tomatoCountedPrice + mozzarellaCountedPrice + saladCountedPrice

print(sumOfCalories)
print(f"{tomato:<15}, kalorie:{tomatoCountedCalories:7.2f}, b: {tomatoCountedProteins:5.2f}, t: {tomatoCountedFat:5.2f},\
 w: {tomatoCountedCarbo:5.2f}, waga: {str(tomatoWeight) + ' g':5}, koszt: {str(tomatoCountedPrice):<5} {currency}")
print(f"{mozzarella:<15}, kalorie:{mozzarelaCountedCalories:7.2f}, b: {mozzarellaCountedProteins:5.2f}, t: {mozzarelaCountedFat:5.2f},\
 w: {mozzarellaCountedCarbo:5.2f}, waga: {str(mozzarellaWeight) + ' g':5}, koszt: {str(mozzarellaCountedPrice):<5} {currency}")
print(f"{salad:<15}, kalorie:{saladCountedCalories:7.2f}, b: {saladCountedProteins:5.2f}, t: {saladCountedFat:5.2f}, \
w: {saladCountedCarbo:5.2f}, waga: {str(saladWeight) + ' g':5}, koszt: {str(saladCountedPrice):<5} {currency}")
print("="*93)


print(f"{sum:<15}, kalorie:{sumOfCalories:7.2f}, b: {sumOfProteins:5.2f}, t: {sumOfFats:5.2f}, w: {sumOfCarbos:5.2f},\
 waga:{str(sumOfWeights) + ' g':5}, koszt: {str(sumOfPrices):<5} {currency}")