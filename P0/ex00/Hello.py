ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#ft_list
ft_list.pop()
ft_list.append("World!")

#ft_tuple, hay que pasarlo a una lista porque los tuples son inmutables
tuple_to_list = list(ft_tuple)
tuple_to_list.pop()
tuple_to_list.append("Spain!")
ft_tuple = tuple(tuple_to_list)

#ft_set, añade Maálga en el orden que quiere porque los sets no tienen orden
ft_set.remove("tutu!")
ft_set.add("Málaga!")

#ft_dict
ft_dict["Hello"] = "42Málaga!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)