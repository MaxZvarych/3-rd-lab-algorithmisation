def form_tribes(list_of_pairs):
    tribes = []
    if len(list_of_pairs)!=0:
        for pair in list_of_pairs:
            if pair[0]==0 or pair[1]==0:
                continue
            else:
                tribes.append([pair[0], pair[1]])
                break
        i = 0
        for pair in list_of_pairs:
            if pair[0]==0 or pair[1]==0:
                continue
            if i == 0:
                i += 1
                continue
            for tribe in tribes:
                if pair[0] in tribe:
                    tribe.append(pair[1])
                    break
                elif pair[1] in tribe:
                    tribe.append(pair[0])
                    break
                continue
            else:
                tribes.append([pair[0], pair[1]])
    return tribes


def calculate_amount_of_boys_and_girls(tribe):
    girls_amount = 0
    for tribe_member in tribe:
        if tribe_member % 2 == 0:
            girls_amount += 1
    boys_amount = len(tribe) - girls_amount
    return girls_amount, boys_amount


def calculate_result(tribes):
    boys_amount_in_each_tribe = [calculate_amount_of_boys_and_girls(tribe)[1] for tribe in tribes]
    girls_amount_in_each_tribe = [calculate_amount_of_boys_and_girls(tribe)[0] for tribe in tribes]
    boys_amount = 0
    girls_amount = 0
    sum = 0
    for boy in boys_amount_in_each_tribe:
        boys_amount += boy
    for girl in girls_amount_in_each_tribe:
        girls_amount += girl
    for tribe in tribes:
        sum += calculate_amount_of_boys_and_girls(tribe)[0] * calculate_amount_of_boys_and_girls(tribe)[1]
    return boys_amount * girls_amount - sum


