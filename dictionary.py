# dictionary : -  a changable , unordered collection of unique key : value 
# pairs fast because they use hashing dict allows us to access the value fast


# syntax : dict = {keys :values}
# print(dict.keys())   will print all the keys of the dictionary
#print(dict.values()) will print all the values of the dictionary
name = {'piyush':'yadav' , 
        'abhishek' :'sing' ,
        'yash' :'gaikwad',
        'rushi' : 'darveshwar',
        'sumi' : 'kekal'}

print(name['piyush']) #accesing the values
print(name.get('germany'))#more safer way to acces or find oout if athing exist or not

#.pop(key) to remove , .clear() to delete the dictionary