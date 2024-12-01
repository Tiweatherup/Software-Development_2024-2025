class UserInputValidator:
  

    def validate_positive_integers(self, input_list):
        
        valid_integers = []
        for item in input_list:
            try:
                num = int(item)
                if num > 0:
                    valid_integers.append(num)
            except ValueError:
                pass  
        return valid_integers

    def display_validation_message(self, input_list):
        
        valid_integers = self.validate_positive_integers(input_list)
        if valid_integers:
            print("The list contains valid positive integers:", valid_integers)
        else:
            print("The list does not contain any valid positive integers.")



#validator = UserInputValidator()
#input_strings = [ "abc", "0", "-5", "3.14"]
#validator.display_validation_message(input_strings)