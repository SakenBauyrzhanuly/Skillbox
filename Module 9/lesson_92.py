import os

def print_dirs(project):
    print('\n Содержимое директории', project)
    if os.path.exists(project):
        for i_elem in os.listdir(project):
            path = os.path.join(project, i_elem)
            print('  ', path)
    else:
        print('Каталога не существует')




projects_list = ['Prod', 'Skilbox_git', 'Skillbox']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
    print_dirs(path_to_project)