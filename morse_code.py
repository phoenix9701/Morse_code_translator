#this line of code defines that we have declared a dictionary where key is the alphabet and the answer to key is morse code of particular alphabet
MORSE_CODE={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',',':'--..--','.':'.-.-.-','?':'..--..','/':'-..-.','-':'-....-','(':'-.--.',')':'-.--.-'}
#this function encrypts the message 
def encoder(message):
    encoded =''
    #this loop arranges the letters of encrypted message in ascending order separately and combines them back together 
    for letter in message:
        if letter != ' ':
            encoded += MORSE_CODE[letter] + ' '
        else:
    encoded += ' '
    #this function gives the encrypted message as output
    print("encoded message: ",encoded)
    menu()
    #this function decrypts the encrypted message 
def decryption(message):
   message += ' '
   decipher = ''
   mycitext = ''
   for myletter in message:
      # checks for space
      if (myletter != ' '):
         i = 0
         mycitext += myletter
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(mycitext)]
            mycitext = ''
            #this function gives the decrypted message as output 
   print("decoded message:",decipher)
   menu()
def menu():
    print("""
        ##################################################
        ##################################################
                MORSE CODE ENCODER , DECODER
        ##################################################
                           OPTIONS
        --------------------------------------------------
            1) Translate into morse-code
            2) Translate morse-code into simple text
            3) exit
        --------------------------------------------------
        --------------------------------------------------
          """)
    choice=input("enter the option number: ")
    if choice=='1':
        msg=input("enter your message")
        encoder(msg.upper())
    elif choice=='2':
        msg=input("enter you message in morse-code")
        decryption(msg)
    elif choice=='3':
        print("exit")
        exit()
    else:
        print("enter a valid choice")
        menu()
menu()
