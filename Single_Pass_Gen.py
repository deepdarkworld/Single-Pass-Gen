import string
import random
import sys 
import time 
import os  

text = '''
#########################################
# Author : RD Durjoy (DeepDarkWorld)     #
# Team   : Knight Squad                  #
# Date   : 11 - 04 - 2020                #
# CEO :    Noman Prodhan                 #
#########################################  
'''
print(text)
if __name__ == '__main__':
    str_a = string.ascii_letters
    str_b = string.ascii_lowercase
    str_c = string.ascii_uppercase
    str_d = string.digits
    str_e = string.punctuation

    input_user = int(input("Enter Your Password len(minimum:10) :\n"))


    s_SDR = []
    s_SDR.extend(str_a)
    s_SDR.extend(str_b)
    s_SDR.extend(str_c)
    s_SDR.extend(str_d)
    s_SDR.extend(str_e)
    # print(s_SDR)
    random.shuffle(s_SDR)
    # print(s_SDR)
    print("\nYour Password Is:")
    print("".join(s_SDR[0:input_user]))





