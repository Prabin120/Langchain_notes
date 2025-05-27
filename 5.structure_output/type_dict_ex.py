from typing import TypedDict

class Person(TypedDict):
    name: str
    age: str

new_person : Person = {
    'name': 'Nitish',
    'age': 35
}

print(new_person)