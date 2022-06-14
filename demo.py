from port import Port
from commands import Commands, Support
from graph import StandGraph
import matplotlib.pyplot as plt

import sys
import time


class Demo:
    demo_running_status = False
    demo_lines_limit = Commands.lines_limit
    demo_timeout = Commands.timeout_ms
    picture_num = 0

    @staticmethod
    def start_demo():
        if not Port.check_port_open():
            print('Demo not started. No port connection')
        else:
            # demo variables
            print('Demo started')
            Port.send_line(Commands.start_cycle_output)
            Demo.demo_running_status = True
            counter = 0
            start_time = Support.current_milli_time()
            current_time = Support.current_milli_time()
            first_record = True
            current_input = ''

            # graph creating
            demo_graph = StandGraph()

            while Demo.demo_running_status:
                new_input = Port.read_line()
                if new_input == Commands.stop_cycle_income:
                    print('Demo stopped by income signal')
                    Demo.demo_running_status = False

                elif Commands.check_if_data(new_input) and new_input != current_input:
                    if first_record:
                        first_record = False
                        start_time = Support.current_milli_time()
                        demo_graph.start_animation()

                    # getting data from port
                    current_input = new_input
                    read2 = new_input.split(' ', 1)
                    current_time = Support.current_milli_time()
                    ms = current_time - start_time
                    result_str = str(f'{ms} {read2[-1]}\n')
                    data_list = result_str.split()

                    # graph update
                    demo_graph.update_data(data_list)
                    demo_graph.update_graphic()

                    counter += 1

                    # stop cycle by line limit
                    if counter >= Demo.demo_lines_limit:
                        picture_name = str(f'demo_charta_{Demo.picture_num}.png')
                        Demo.picture_num += 1
                        demo_graph.finish_data(picture_name, Commands.graph_show_time)
                        demo_graph.finish_animation()
                        print('Demo stopped by line limit')
                        Demo.demo_running_status = False

                # stop cycle by timeout
                if Support.current_milli_time() - current_time > Demo.demo_timeout:
                    if counter > 0:
                        picture_name = str(f'demo_charta_{Demo.picture_num}.png')
                        Demo.picture_num += 1
                        demo_graph.finish_data(picture_name, Commands.graph_show_time)
                        demo_graph.finish_animation()
                        print('Demo stopped by line limit')
                    print('Demo stopped. Timeout.')
                    Demo.demo_running_status = False
