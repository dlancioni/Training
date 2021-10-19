from common import person1, greeting

person1["name"] = "David Lancioni"

print(person1["name"])

print(greeting("David"))

d = {
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
}
print(type(d))