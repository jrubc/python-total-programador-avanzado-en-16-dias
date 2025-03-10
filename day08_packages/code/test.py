def decorate_greet(function):

    def other_function(word):
        print("Hello")
        function(word)
        print("Goodbye")

    return other_function


def upper_case(text):
    print(text.upper())


def lower_case(text):
    print(text.lower())


upper_case_decorated = decorate_greet(upper_case)

upper_case("jorge")
upper_case_decorated("jorge")
