names = ['Tom', 'Bob', 'Albert']
ages = [20, 45, 60]

people = dict(zip(names, ages))
print(people)

# for i_person in people:
#     print(i_person)
people_2 = {
    i_name: i_age + 10
    for i_name, i_age in zip(names, ages)
}
print(people_2)