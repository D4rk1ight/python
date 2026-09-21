# user_input = input("Enter some-thing ")


def check_type(user_input):
    return type(user_input).__name__


print(check_type(user_input))
