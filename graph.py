import matplotlib.pyplot as plt
import time


class StandGraph:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.y0 = 0
        self.y1 = 0
        self.x_list = []
        self.y_list = []
        self.yy_list = []
        self.yyy_list = []

    @staticmethod
    def start_animation():
        plt.ion()

    def update_data(self, data_list):
        self.x = float(data_list[0])
        self.y = float(data_list[4])
        self.y0 = float(data_list[5])
        self.y1 = float(data_list[6])
        print(self.x)
        print(self.y)
        print(self.y0)
        print(self.y1)
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        self.yy_list.append(self.y0)
        self.yyy_list.append(self.y1)

    def update_graphic(self):
        plt.plot(self.x_list, self.y_list, color='green')
        plt.plot(self.x_list, self.yy_list, color='red')
        plt.plot(self.x_list, self.yyy_list, color='blue')
        # plt.scatter(x, y, c = 'r')
        # plt.scatter(x, y0 ,c = 'g')
        # plt.scatter(x, y1, c = 'b')
        plt.title('Pressure')
        plt.xlabel('time ms')
        plt.ylabel('bar')
        # plt.subplot(311)
        plt.plot(self.x, self.y, color='blue', label="cosine")
        # plt.subplot(312)
        # plt.plot(x ,y0)
        # plt.subplot(313)
        # plt.plot(x ,y1)
        plt.grid(True)
        plt.pause(0.001)
        plt.draw()

    @staticmethod
    def finish_data(file_name, sleep_time):
        plt.savefig(file_name)
        time.sleep(sleep_time)

    @staticmethod
    def finish_animation():
        plt.ion()
