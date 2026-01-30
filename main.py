import qrcode



print("what link do you want me to create the qrcode")

data = input('enter link: ')


img = qrcode.make(data)

name_for_qrcode = input("what do you want your qr code name to be?: ")



img.save(f"{name_for_qrcode}.png")

if qrcode.make == True:
    print("an error occurred please try again.")
else:
    print("your qrcode has been created successfully")




