class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.child_list = []

    def add_child(self, child):
        self.child_list.append(child)

    def print_info(self):
        print(
            'Имя родителя: {}\nВозраст родителя: {}\nСписок детей: \n'.format(
                self.name, self.age,

            )
        )


    def feed_child(self):
        for i_child in self.child_list:
            if i_child.state_feed_type == 'hungry':
                i_child.state_feed_type = 'not hungry'
                return i_child.state_feed_type
            else:
                print('Ребенок не голоден')


    def calm_down(self):
        for i_child in self.child_list:
            if i_child.state_calm_type == 'cry':
                i_child.state_calm_type = 'happy'
                return i_child.state_calm_type
            else:
                print('Ребенок спокоен')


class Child:

    def __init__(self, name_child, age_child, state_calm, state_feed):
        self.name_child = name_child
        self.age_child = age_child
        self.state_calm_type = state_calm
        self.state_feed_type = state_feed

    def __str__(self):
        return f'Имя: {child_1.name_child, child_2.name_child}, Возраст: {child_1.age_child, child_2.age_child}, Спокоен: {child_1.state_calm_type, child_2.state_calm_type}, Голоден: {child_1.state_feed_type, child_2.state_feed_type}'


mother = Parent('Sara', 45)
father = Parent('John', 48)
child_1 = Child('Ben', 15, 'cry', 'hungry')
child_2 = Child('Nen', 19, 'cry', 'hungry')


mother.add_child(child_1)
mother.add_child(child_2)

mother.calm_down()
mother.print_info()

print(str(child_1))
