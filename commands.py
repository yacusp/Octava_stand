# commands and list
import time


class Commands:
    gear_up_output = b'50'
    gear_down_output = b'51'
    start_cycle_output = b'2345'
    start_cycle_income = ' button triggered'
    stop_cycle_income = 'cycle end'

    @staticmethod
    def check_if_data(input_command):
        try:
            split_input = input_command.split()
            if Commands.is_number(split_input[0]):
                return True
            else:
                return False
        except AttributeError:
            return False

    @staticmethod
    def is_number(num):
        try:
            float(num)
            return True
        except ValueError:
            return False


class Support:
    @staticmethod
    def current_milli_time():
        return round(time.perf_counter_ns() / 1000000)
