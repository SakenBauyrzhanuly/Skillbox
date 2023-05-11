students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def get_interests_length(student_dict):
    interests = {interest for student in student_dict.values() for interest in student['interests']}
    length_fio = sum(len(i_len['surname']) for i_len in student_dict.values())
    return interests, length_fio
id_ages = [(id, students[id]['age']) for id in students]
print(id_ages)

my_lst, l = get_interests_length(students)
print('Полный список интересов всех студентов: ', my_lst)
print('Общая длина всех фамилий студентов: ', l)