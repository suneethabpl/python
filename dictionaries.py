person={
    "key":"value",
    # key is typically a string and the value could be literaly anything, it could be a list,integer,float,string.
    "name":"punee",
    "gmail":"punee@gmail.com"
}
print(person['gmail'])
print(person)
person['yahoo']="@coding.for.everybody"
print(person)
del person['key']
print(person)