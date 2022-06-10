# command list

class Commands:
    gear_up_output = b'50'
    gear_down_output = b'51'
    start_record_output = b'2345'

    @staticmethod
    def check_if_data(input_command):
        split_input = input_command.split()
        if Commands.is_number(split_input[0]):
            return True
        else:
            return False

    @staticmethod
    def is_number(num):
        try:
            float(num)
            return True
        except ValueError:
            return False
