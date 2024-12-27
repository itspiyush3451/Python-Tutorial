#string slicing means , creating a substring by extracting a string from another string.
#it is  done by indexing[] or slice().
#[start:stop:step]


#indexing
name = "Piyush Yadav"

first_Name = name[0:6] #the start value is inclusive and the stop value is exclusive i.e [0:n]->deisplays from 0-n-1
last_Name = name[7:12]
funky_Name = name[::2] #the step defines the space between the strings which will be displayed 
reverse_Name = name[::-1] #will generate reverse string
print(first_Name)
print(last_Name)
print(funky_Name)
print(reverse_Name)

# slicing

website1 = "http://google.com"
website2 = "http://twitter.com"
sl = slice(7,-4)  #the negetive index start from the end of the string 
                    # and starts with -1 unlike the starting point which startrs with 0
print(website1[sl])
print(website2[sl])
