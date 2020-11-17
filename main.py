from manager import tribes_evaluator as ev
from additional_files import tribes_reader as reader

if __name__ == '__main__':
    filename = input("Please write filename to get data:")
    #C:\Users\111\PycharmProjects\Algorithmisation(Lab3)\additional_files\input_and_result\tribes.in.txt
    pairs = reader.read_info_from_file(filename)
    tribes=ev.form_tribes(pairs[0])
    ev.calculate_result(tribes)
    result=ev.calculate_result(tribes)
    print("Number of possible marriages:"+str(result))
    reader.write_result_to_file(result)