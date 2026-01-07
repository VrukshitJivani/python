person={'name':'Jay','age':30,'city':'Bhavnager','occupation':'Engineer','salary':90000}
print(person)
print(person['name'])
print(person.get('age'))# if key is not found then retrun null #it is good to use
print(person.get('pincode'))
print(person.keys())# it will return all keys 
print(person.values())# it will return all values
print(person.items())# it will return all items in tuple format
person['pincode']=36401

person2=person.copy()# it will create shallow copy of dictionary
print(person2)

list=['name','age','city','pincode','mobile','email']
person3=dict.fromkeys(list)# it will create dictionary with keys from list and values as none
print(person3)

person3['name']='Jay'
person['age']=34
person3['city']='Bhavnagar'
person3['pincode']=364001
person3['mobile']=1234567890
person3['email']='jay@gmail.com'
print(person3)

person3.pop('email')# it will remove the specified key
print(person3)

person3.pop('email',False)# it will remove the specified key if found otherwise return false
print(person3)

person3.popitem()# it will remove the last inserted key
print(person3)