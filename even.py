def find_Even_Numbers(start_number,end_number):
    list1 = []
    list2 = []
    for number in range(start_number,end_number+1):
        if number % 2 == 0:
            list1.append(number)
        else:
            list2.append(number)
    return ("even : " + str(list1),"odd : "+str(list2))

initial_number = 10
final_number =  50
print(find_Even_Numbers(initial_number,final_number))