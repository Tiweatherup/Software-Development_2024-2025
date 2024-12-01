class UserInputValidator:
    def validate_positive_integers(self, input_list):
        valid_integers = []
        for item in input_list:
                num = int(item)
                if num > 0:
                    valid_integers.append(num)
                return valid_integers

validator = UserInputValidator()
input_strings = ["4", "abcd", "0", "-1", "18", "3.14"]
valid_numbers = validator.validate_positive_integers(input_strings)
print(valid_numbers)