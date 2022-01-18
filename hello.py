def names_func(number):
    switcher = {
        0: "Tim.",
        2: "Dan.",
        1: "John.",
        3: "Amy.",
        4: "Chris.",
        5: "Nobody."
    }

    return switcher.get(number, "default")



for n in range(0, 5):
    print('Hello, ' + names_func(n))
