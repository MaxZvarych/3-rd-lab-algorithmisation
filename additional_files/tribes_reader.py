def read_info_from_file(filename):
    number_of_pairs = 0
    list_of_same_tribe_people = []
    with open(filename, 'r') as tribes:
        i = 0
        for row in tribes:
            if (i != 0):
                tribe_info = row.split()
                list_of_same_tribe_people.append([int(tribe_info[0]), int(tribe_info[1])])
            elif (i == 0):
                number_of_pairs = int(row)
                i += 1
    return list_of_same_tribe_people, number_of_pairs

def write_result_to_file(result):
    number_of_marriages=str(result)
    with open('additional_files\\input_and_result\\tribes.out.txt','w') as  result_file:
        result_file.write(number_of_marriages)