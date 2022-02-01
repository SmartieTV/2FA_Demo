# Demo (lightweight and simple) 2FA and QR-code generator and validator. 

# Inspired by: Jothin kumar's post on dev.to.

#Used for creating and validating 2fa code.
from onetimepass import valid_totp
from secrets import choice
#Used for generating and showing qrcode
import qrcode

def secret_gen(): #Generate a 16-digit secret code. 
  secret = ''
  while len(secret) < 16:
    secret += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
  return secret

secret = secret_gen()
print('Generated code: ' + str(secret))
    
secret_qr = "otpauth://totp/:?secret=" + str(secret) + "&issuer=SMRTV_Democode" #Setting string for qrcode. 
img = qrcode.make(secret_qr) #Making qr-image. 
  
img.save('OTP_qr.png') #Saves a qrcode to scan in 2fa apps, overwriting the old image. 
with open('OTP_txt.txt', 'w') as f: #Saves code to a local textfile, overwriting old file. 
  f.write('Generated OTP code: \n' + str(secret))
  f.close

while True: #Checks the entered OTP with the secret code.
  OTP = int(input('Enter OTP from authentication app: '))
  authenticateSuccessful = valid_totp(OTP, secret) 
  if authenticateSuccessful:
    print("Entered OTP was correct!")
    print("")
  elif not authenticateSuccessful:
    print("Entered OTP was wrong!")
    print("")