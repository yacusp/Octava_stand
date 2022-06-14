from port import Port
from commands import Commands, Support


class Record:
    recording_status = False
    result_file_name = 'test_con.txt'
    record_limit = Commands.lines_limit  # limit of lines to record
    record_timeout = Commands.timeout_ms

    @staticmethod
    def start_record():
        if not Port.check_port_open():
            print('Record not started. No port connection.')
        else:
            print('Record started')
            Port.send_line(Commands.start_cycle_output)
            Record.recording_status = True
            counter = 0
            start_time = Support.current_milli_time()
            current_input = ''

            with open(Record.result_file_name, 'w') as result_file:
                while Record.recording_status:
                    new_input = Port.read_line()
                    if new_input.strip() == Commands.stop_cycle_income:
                        print('Record stopped by income signal')
                        Record.recording_status = False
                    elif Commands.check_if_data(new_input) and new_input != current_input:
                        current_input = new_input
                        input_list = new_input.split(' ', 1)
                        data = input_list[-1].strip()
                        ms = Support.current_milli_time() - start_time
                        result_str = str(f'{ms} {data}\n')
                        result_file.write(result_str)
                        counter += 1
                        if counter >= Record.record_limit:
                            print('Record stopped. Lines limit reached.')
                            Record.recording_status = False

                    if Support.current_milli_time() - start_time > Record.record_timeout and counter == 0:
                        print('Record stopped. Timeout.')
                        Record.recording_status = False
