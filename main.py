import qrcode



print("what link do you want me to create the qrcode")

data = input('enter link: ')


img = qrcode.make(data)

name_for_qrcode = input("what do you want your qr code name to be?: ")



img.save(name_for_qrcode, '.png')





