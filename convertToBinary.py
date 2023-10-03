dec = int(input("Enter the value = "))
binary = ""
while dec > 0:
    remainder = dec % 2
    binary = str(remainder) + binary
    dec = dec // 2
print("binary number is ", binary)