# HASHLIB LIBRARARY :- ITS AN INTERFACE FOR HASHING MESSAGES EASILY 
                    #    CONTAINS NUMEROUS METHODS which will handle hashing any raw message in an encrypted method 

''' PYFIGLET LIBRARY :- ITS A MODULE WHICH TAKE TEXT FROM USER AND DISPLAY IT IN ASCII ART FORMAT 
                        CONSIST OF DIFFERETN TYPES OF FONTS THAT CAN BE USED TO MAKE SCRIPT MORE BEAUTIFUL 

'''

import hashlib 
import sys 
import pyfiglet
ascii_banner = pyfiglet.figlet_format("HASH CRACKER")
print ( ascii_banner) 


# now we will be printing the algot=rithms that the user wil;l choose 

print ("Algorithms available : \n1. MD5 \n2. SHA1 \n3. SHA256 \n4. SHA512 \n5. SHA3_256 \n6. SHA3_512")
hash_type = input ("whats the hash type ? " )
wordlist_location  = str (input("whats the wordlist location ? " ))
hash = str(input (" ENTER THE HASH TO CRACK:- "))

#  NOW DECLARING THE VARIABLE WHICH  WILL OPENT THE FILE OR WORDLIST FILE GIVEN BY THE USER 

word_list = open (f"{wordlist_location}").read()

#  now in another list list we will take the word list provided by the user and split it into lines

list = word_list.splitlines()
for word in list :
    if hash_type== "MD5" :
        hash_object = hashlib.md5(f"{word}".encode("utf-8"))
        hashed_word = hash_object.hexdigest()
        if hashed_word == hash :
            print (f"\033[1;32m hash Cracked ! The word is : {word} ")
            
    elif hash_type == "SHA1" :
         hash_object = hashlib.sha1(f"{word}".encode("utf-8"))
         hashed_word = hash_object.hexdigest()
         if hashed_word == hash :
            print (f"\033[1;32m hash Cracked ! The word is : {word} ")


    elif hash_type == "SHA256" :
         hash_object = hashlib.sha256(f"{word}".encode("utf-8"))
         hashed_word = hash_object.hexdigest()
         if hashed_word == hash :
            print (f"\033[1;32m hash Cracked ! The word is : {word} ")        


    elif hash_type == "SHA512" :
         hash_object = hashlib.sha512(f"{word}".encode("utf-8"))
         hashed_word = hash_object.hexdigest()
         if hashed_word == hash :
            print (f"\033[1;32m hash Cracked ! The word is : {word} ")



    elif hash_type == "SHA3_256" :
         hash_object = hashlib.sha3_256(f"{word}".encode("utf-8"))
         hashed_word = hash_object.hexdigest()
         if hashed_word == hash :
            print (f"\033[1;32m hash Cracked ! The word is : {word} ")




    elif hash_type == "SHA3_512" :
         hash_object = hashlib.sha3_512(f"{word}".encode("utf-8"))
         hashed_word = hash_object.hexdigest()
         if hashed_word == hash :
            print (f"\033[1;32m hash Cracked ! The word is : {word} ")






    