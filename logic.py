squareFeetWallSpace901297=float(input("please enter the square feet wall space"))
priceOfPaintPerGallon901297=float(input("please enter the price of paint per gallon"))

#the hours of labor required
theHoursOfLaborRequired901297= squareFeetWallSpace901297 / 150 * 9
print(f"the hours of labor required : {theHoursOfLaborRequired901297}")

def  produceNum(squareFeetWallSpace901297):
     if squareFeetWallSpace901297>2000:
         # calculate the labor price
         laborCharges=theHoursOfLaborRequired901297*25
     if squareFeetWallSpace901297<=2000:
         laborCharges=theHoursOfLaborRequired901297*30
     return laborCharges

#the labor price
laborcharges901297=produceNum(squareFeetWallSpace901297)
print(f"the labor charges : {laborcharges901297}")


#the number of gallons of paint required
numberOfGallonsOfPaintRequired901297=squareFeetWallSpace901297 / 150
print(f"the number of gallons of paint required : {numberOfGallonsOfPaintRequired901297}")

# the cost of paint
costOfPaint901297=numberOfGallonsOfPaintRequired901297*priceOfPaintPerGallon901297
print(f"the cost of paint: {costOfPaint901297}")

#the total cost of paint job
totalCostOfPaintJob901297=costOfPaint901297+laborcharges901297;
print(f"the total cost of paint job: {totalCostOfPaintJob901297}")