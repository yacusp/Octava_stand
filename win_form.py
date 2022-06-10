from tkinter import *
from tkinter.ttk import Combobox
from port import Port
from commands import Commands
from record import Record


class StandForm:
    def __init__(self, win):
        # port and speed labels
        self.port_label = Label(win, text="Порт", width=15, height=1)
        self.port_label.grid(row=0, column=0, padx=20, pady=10, sticky=W + E)
        self.speed_label = Label(win, text="Скорость", width=15, height=1)
        self.speed_label.grid(row=0, column=1, padx=20, pady=10, sticky=W + E)

        # port and speed comboboxes
        self.port_combo = Combobox(win, width=15, height=1)
        self.port_combo['values'] = tuple(Port.serial_ports())
        self.port_combo.current(0)  # установите вариант по умолчанию
        self.port_combo.grid(row=1, column=0)
        self.speed_combo = Combobox(win, width=15, height=1)
        self.speed_combo['values'] = Port.speeds
        self.speed_combo.current(2)  # установите вариант по умолчанию
        self.speed_combo.grid(row=1, column=1)

        # connecting button
        self.connect_btn = Button(win, text="Подключиться", width=30, height=1, command=self.connect_button)
        self.connect_btn.grid(row=2, columnspan=2, padx=20, pady=10)

        # backup of button's original background color
        self.orig_button_color = self.connect_btn.cget("background")

        # some empty space between buttons
        self.frame1 = Frame(win, height=40)
        self.frame1.grid(row=3)

        self.low_btn = Button(win, text="Опустить", width=15, height=1, command=self.gear_down_button)
        self.low_btn.grid(row=4, column=0, padx=20, pady=10)
        self.up_btn = Button(win, text="Поднять", width=15, height=1, command=self.gear_up_button)
        self.up_btn.grid(row=4, column=1, padx=20, pady=10)

        self.record_btn = Button(win, text="Записать", width=15, height=1, command=self.start_record_button)
        self.record_btn.grid(row=5, column=0, padx=20, pady=10)

        self.record_btn = Button(win, text="Демо", width=15, height=1, command=self.start_demo_button)
        self.record_btn.grid(row=5, column=1, padx=20, pady=10)

        #self.new_port = Port(self.port_combo.get(), self.speed_combo.get())

    def connect_button(self):
        print('Connect button clicked!')
        if not Port.connected_status:
            Port.set_port(self.port_combo.get())
            Port.set_speed(self.speed_combo.get())
            Port.connect()
            self.connect_btn.config(bg='green', text='Отключиться')

        else:
            self.connect_btn.config(bg=self.orig_button_color, text='Подключиться')
            Port.disconnect()

    def gear_up_button(self):
        self.new_port.send_command(Commands.gear_up_output)
        print('Gear up button clicked!')

    def gear_down_button(self):
        self.new_port.send_command(Commands.gear_down_output)
        print('Gear down button clicked!')

    def start_record_button(self):
        print('Start record button clicked!')

    def start_demo_button(self):
        print('Start demo button clicked!')

def main():
    window = Tk()
    window.title("Стенд испытания шасси")
    #window.geometry('310x300')
    app = StandForm(window)
    #print('Check')
    window.mainloop()


if __name__ == '__main__':
    main()
