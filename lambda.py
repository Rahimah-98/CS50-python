people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho","house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Hermione", "house": "Gryffindor"},
]

def f(person):
    return person["name"]

# people.sort(key=f, reverse=True)
people.sort(key=lambda person: person["name"])

print(people)