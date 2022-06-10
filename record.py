import time

class Record:
    recording_status = False
    result_file_name = 'test_con.txt'
    record_limit = 200

    @staticmethod
    def start_record():
        Record.recording_status = True
        counter = 0
        start_time = Record.current_milli_time()

        with open(Record.result_file_name, 'a') as result_file:
            while Record.recording_status:




        result_file = str('result_' + Record.result_file_num + '.txt')

    @staticmethod
    def current_milli_time():
        return round(time.time() * 1000)