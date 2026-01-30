import qrcode



print("what link do you want me to create the qrcode")

data = input('')





img = qrcode.make(data)
name_for_qrcode = input('')
img.save('name_for_qrcode'.png)

