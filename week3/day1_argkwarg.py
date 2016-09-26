def adder(number_two, number_one, message="No Message Passed", happy=True):
    print(message)
    return number_one + number_two


print(adder(9, 4, happy=False, message="DO MATH SON"))

print(adder("Joel", " likes programming!"))


def add(*args):
    # return number_one + number_two + number_three
    return sum(args)


print(add(1, 2, 4, 90))

print(adder(*[9, 4]))

print(add(*range(1000)))


# ??
def beginners_luck(name, account_number, *args, birthday="tommorow", **kwargs):
    print(name, "NAME")
    print(account_number, "ACCOUNT NUMBER")
    print(args)
    print(kwargs)
    return 1

print(beginners_luck("joel", 12345678, [1, 2, 3], 99, birthday="Today", lol="joel"))
