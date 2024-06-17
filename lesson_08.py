def sum_numbers_in_string(s):
    try:

        numbers = map(int, s.split(','))

        return sum(numbers)
    except ValueError:

        return "Не можу це зробити!"


input_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


for item in input_list:
    result = sum_numbers_in_string(item)
    print(result)
