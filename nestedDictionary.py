family = {
    "son":"yash",
    "daughter":"aish",
    "parent":{
        "mother":"mangal",
        "father":"sunil"
    },
    "skills":["js"]
}
#add values in list
family["skills"].append("java")
print(family)
#{'son': 'yash', 'daughter': 'aish', 'parent': {'mother': 'mangal', 'father': 'sunil'}, 'skills': ['js', 'java']}

# retrive nested value
print(family["parent"]["father"]) #sunil

print(family.get("parent"))#{'mother': 'mangal', 'father': 'sunil'}
# print(family.get("parent"))

#add key and value in nested dictionary
family["parent"]["grandmother"] = "anu"
print(family["parent"]) #{'mother': 'mangal', 'father': 'sunil', 'grandmother': 'anu'}

# update nested value
family["parent"]["father"] = "sunil D"
print(family["parent"]["father"]) #sunil D

#delete nested value
del family["parent"]["mother"]
print(family["parent"]) #{'father': 'sunil D' 'grandmother': 'anu'}
