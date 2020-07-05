def func(camel_strings):
    print(camel_strings)
    lower_case = camel_strings.lower()
    camel_split = lower_case.split(' ')
    print("_".join(camel_split))
    print( '-'.join(camel_split))


camel = "This Is Camel Cased"
func(camel)