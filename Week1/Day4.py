
country = "japan"
country = "usa"
country = "nepal"

countries = ["japan", "usa", "nepal"] # Lists
# print(countries[-1])
# countries.append("india") -- adds to last of list
# countries.pop() -- removes last element of list
# countries.insert(0, "india") -- adds to first index
# countries.remove("usa")
# countries[1] = "china"
# print(len(countries))
# print(countries)

# Sets
countries_sets = {"japan", "usa", "nepal", "japan"} # sets
print(countries_sets)


# Tuples -> tapaiko data or value unchangeable cha vane its best to use tuple.
countries_tuples = ("japan", "usa", "nepal", "japan") # tuples
# print(countries_tuples[0])
# countries_tuples[1] = "china" # this doesnot work because tuples are immutable
# print(countries_tuples.count("japan"))
# print(countries_tuples.index("japan"))

# Dictionary
person_info = {
    "full_name" : "santosh bastola",
    "address" : "pokhara",
    "age" : 26,
    "company" : "digital pathshala",
    "isNepali": True
}

print(person_info["full_name"])
person_info["color"] = "blue"
person_info["age"] = 27
person_info.pop("company")
print(person_info)
