from tkinter import *
from tkinter.ttk import Combobox
from port import Port
from commands import Commands
from record import Record
from demo import Demo


class StandForm:
    glob_width = 40  # should be even
    glob_half_width = int(glob_width / 2)

    def __init__(self, win):
        # port and speed labels
        self.port_label = Label(win, text="Порт", width=StandForm.glob_half_width, height=1)
        self.port_label.grid(row=0, column=0, padx=20, pady=10, sticky=W + E)
        self.speed_label = Label(win, text="Скорость", width=StandForm.glob_half_width, height=1)
        self.speed_label.grid(row=0, column=1, padx=20, pady=10, sticky=W + E)

        # port and speed comboboxes
        self.port_combo = Combobox(win, width=StandForm.glob_half_width, height=1)
        self.port_combo['values'] = tuple(Port.serial_ports())
        self.port_combo.current(0)  # установите вариант по умолчанию
        self.port_combo.grid(row=1, column=0)
        self.speed_combo = Combobox(win, width=StandForm.glob_half_width, height=1)
        self.speed_combo['values'] = Port.speeds
        self.speed_combo.current(0)  # установите вариант по умолчанию
        self.speed_combo.grid(row=1, column=1)

        # connecting button
        self.connect_btn = Button(win, text="Подключиться", width=StandForm.glob_width,
                                  height=1, command=self.connect_button)
        self.connect_btn_pressed = False
        self.connect_btn.grid(row=2, columnspan=2, padx=20, pady=10)

        # backup of button's original background color
        self.orig_button_color = self.connect_btn.cget("background")

        # some empty space between buttons
        self.frame1 = Frame(win, height=40)
        self.frame1.grid(row=3)

        # Gear down and gear up buttons
        self.low_btn = Button(win, text="Опустить", width=StandForm.glob_half_width,
                              height=1, command=self.gear_down_button)
        self.low_btn.grid(row=4, column=0, padx=20, pady=10)
        self.up_btn = Button(win, text="Поднять", width=StandForm.glob_half_width,
                             height=1, command=self.gear_up_button)
        self.up_btn.grid(row=4, column=1, padx=20, pady=10)

        # Record start button
        self.record_btn = Button(win, text="Записать", width=StandForm.glob_half_width,
                                 height=1, command=self.start_record_button)
        self.record_btn.grid(row=5, column=0, padx=20, pady=10)
        self.record_btn_pressed = False

        # Demo start button
        self.demo_btn = Button(win, text="Демо", width=StandForm.glob_half_width,
                               height=1, command=self.start_demo_button)
        self.demo_btn.grid(row=5, column=1, padx=20, pady=10)
        self.demo_btn_pressed = False

        # self.new_port = Port(self.port_combo.get(), self.speed_combo.get())

    def connect_button(self):
        print('Connect button clicked!')
        if not Port.check_port_open():
            Port.set_port(self.port_combo.get())
            Port.set_speed(self.speed_combo.get())
            Port.connect()
            self.connect_btn.config(bg='green', text='Отключиться')
            self.connect_btn_pressed = True

        else:
            self.connect_btn.config(bg=self.orig_button_color, text='Подключиться')
            self.connect_btn_pressed = False
            Port.disconnect()

    @staticmethod
    def gear_up_button():
        print('Gear up button clicked!')
        if not Port.check_port_open():
            print('Gear up command was not send. No port connection')
        else:
            Port.send_line(Commands.gear_up_output)

    @staticmethod
    def gear_down_button():
        print('Gear down button clicked!')
        if not Port.check_port_open():
            print('Gear down command was not send. No port connection')
        else:
            Port.send_line(Commands.gear_down_output)

    def start_record_button(self):
        print('Start record button clicked!')
        if not Record.recording_status and not Demo.demo_running_status:
            Record.start_record()
            self.record_btn.config(bg='green', text='Запись идёт')
            self.record_btn_pressed = True
        else:
            if Record.recording_status:
                print('Record already running!')
            elif Demo.demo_running_status:
                print('Demo already running!')

    def record_button_restart(self):
        print('Record button restored')
        self.record_btn.config(bg=self.orig_button_color, text='Записать')
        self.record_btn_pressed = False

    def start_demo_button(self):
        print('Start demo button clicked!')
        if not Record.recording_status and not Demo.demo_running_status:
            Demo.start_demo()
            self.demo_btn.config(bg='green', text='Демо мдёт')
            self.demo_btn_pressed = True
        else:
            if Record.recording_status:
                print('Record already running!')
            elif Demo.demo_running_status:
                print('Demo already running!')

    def demo_button_restart(self):
        print('Demo button restored')
        self.demo_btn.config(bg=self.orig_button_color, text='Демо')
        self.demo_btn_pressed = False


def main():
    window = Tk()
    window.title("Стенд испытания шасси")
    # window.geometry('310x300')
    app = StandForm(window)
    # print('Check')
    window.mainloop()


if __name__ == '__main__':
    main()
