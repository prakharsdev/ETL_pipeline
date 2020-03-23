
#this is a function - definition
#parameters and arguments are same thing
def myFunctionPrakharCool(my_first_parameter, my_second_parameter):
    #integer based tuple
    my_tuple = (1, 2, 3, 4, 5, 6)
    print(my_tuple[0])

    my_tuple = ("1", "2", "3", "4", "5", "6")

    #dictionary | key and value is separated by :
    my_dictionary = {"Age":"45", "Name":"Prakhar" }
    print(my_dictionary["Age"])


    #list
    my_list = ["Flour","Harpic","Eggs","Chocolate"]
    my_list.append(my_first_parameter)
    my_list.append(my_second_parameter)
    print(my_list)

#function invocation - function definition is required before it is invoked
myFunctionPrakharCool("Dahi","Daal")