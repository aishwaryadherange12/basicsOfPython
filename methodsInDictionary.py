# copy() create different memory
# clear()
# clear keys and 
# update
person = {
    "fname":"aish",
    "lname":"dherange",
    "age":23
}
person.update({"age":45,"fname":"a"})
person.pop("age")
print(person)

keys = ["s1","s2"]
d.fromKeys(keys)
print(d)