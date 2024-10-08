#input spending for each category
print("Input the amounts for different spending categories.")
housing = float(input("\tHousing: $"))
utilities = float(input("\tUtilities: $")) 
groceries = float(input("\tGroceries: $"))
transportation = float(input("\tTransportation: $"))
healthCare = float(input("\tHealth Care: $"))
personalCare = float(input("\tPersonal Care: $"))
clothing = float(input("\tClothing: $"))
debt = float(input("\tDebt: $"))
#calculates the total budget
total = housing + utilities + groceries + transportation + healthCare + personalCare + clothing + debt
#print(total)
# calculate % of budget in each category
housingPercent = housing/total  *100
utilitiesPercent = utilities/total *100
groceriesPercent = groceries/total *100
transportationPercent =transportation/total *100
healthCarePercent = healthCare/total *100
personalCarePercent = personalCare/total *100
clothingPercent = clothing/total *100
debtPercent = debt/total *100
#the percentage of the total budget spent in each category
print("The percentage of the total budget spent in each category.")
print(f"\tHousing: {housingPercent}%\n\tUtilities: {utilitiesPercent}%\n\tGroceries: {groceriesPercent}%\n\tTransportation: {transportationPercent}%")
print(f"\tHealth Care: {healthCarePercent}%\n\tPersonal Care: {personalCarePercent}%\n\tClothing: {clothingPercent}%\n\tDebt: {debtPercent}%")