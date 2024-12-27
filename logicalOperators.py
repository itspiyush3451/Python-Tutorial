#(and , or , not)   are the three logical operators :
# In ( and )  both the conditions must be true 
# In ( or )   only one condition must be true
# In ( not )   true becomes false and false becomes true


temp = int(input("what is the temp there bro?:"))

if not(temp> 0  and temp < 30):
    print("The temp is real bad bro , dont go outside ,  you'll get fkd .")
    
elif not(temp < 0 or temp>30):
    print("The temp is all good , you are good to go vro.")