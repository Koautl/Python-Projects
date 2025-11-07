subtotal=0
tax=0
total=0

while True:
    item = input("How much?\n")
    if item.isdigit()==False:
        break

 
    subtotal+=int(item)

tax=int(subtotal)*0.06625
total = int(tax+subtotal)

print("The Subtotal is",subtotal,"\nThe Tax is",tax,"\nThe Grand Total is",total)