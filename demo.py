from port import Port
from commands import Commands, Support
import matplotlib.pyplot as plt


class Demo:
    demo_running_status = False
    demo_lines_limit = 200

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
            current_input = ''

            # graphics variables
            x_list = []
            y_list = []
            yy_list = []
            yyy_list = []
            plt.ion()

            while Demo.demo_running_status:
                new_input = Port.read_line()
                if new_input == Commands.stop_cycle_income:
                    print('Demo stopped by income signal')
                    Demo.demo_running_status = False

                elif Commands.check_if_data(new_input) and new_input != current_input:
                    current_input = new_input
                    read2 = new_input.split(' ', 1)
                    ms = Support.current_milli_time() - start_time
                    result_str = str(f'{ms} {read2[-1]}\n')

                    x = float(result_str.split()[0])
                    y = float(result_str.split()[4])
                    y0 = float(result_str.split()[5])
                    y1 = float(result_str.split()[6])
                    print(x)
                    print(y)
                    print(y0)
                    print(y1)
                    x_list.append(x)
                    y_list.append(y)
                    yy_list.append(y0)
                    yyy_list.append(y1)
                    plt.plot(x_list, y_list, color='green')
                    plt.plot(x_list, yy_list, color='red')
                    plt.plot(x_list, yyy_list, color='blue')

                    # plt.scatter(x, y, c = 'r')
                    # plt.scatter(x, y0 ,c = 'g')
                    # plt.scatter(x, y1, c = 'b')

                    plt.title('Pressure')
                    plt.xlabel('time ms')
                    plt.ylabel('bar')
                    # plt.subplot(311)
                    plt.plot(x, y, color='blue', label="cosine")
                    # plt.subplot(312)
                    # plt.plot(x ,y0)
                    # plt.subplot(313)
                    # plt.plot(x ,y1)
                    plt.grid(True)
                    plt.pause(0.001)
                    plt.draw()

                    counter += 1

                    if counter >= Demo.demo_lines_limit:
                        print('Demo stopped by line limit')
                        Demo.demo_running_status = False

            plt.ioff()
            plt.show()
