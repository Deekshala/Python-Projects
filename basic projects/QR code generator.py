import qrcode
user_link=input("Enter the text or URL for the QR code: ")
file_name=input("Enter the name of the file: ")
qr = qrcode.make(user_link)
qr.save(file_name)
print("QR code saved as: ",file_name)