#Define a Dictionary for Item Prices
itemPrices = {
    "Iphone": 800,
    "Sansung": 900,
    "Nokia": 300
}

#Define a Shopping Cart List:
shoppingCart = [{
    "itemName":"Iphone", 
    "itemQuantity": 12
},
{
    "itemName":"Sansung",
    "itemQuantity": 15
},
{
    "itemName":"Nokia",
    "itemQuantity": 10
}
]

#Define a Price Calculation Function:
def calculatePrice(itemName,itemQuantity):
    if itemName in itemPrices:
        return itemPrices[itemName] * itemQuantity
    else:
             return 0.0

totalPrice = 0.0            

#Calculate the Total Price:
for item in shoppingCart:
    
    totalPrice += calculatePrice(item["itemName"], item["itemQuantity"])
print("The total price of the shopping cart is: ${:.2f}".format(totalPrice))