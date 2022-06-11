# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from win_form import StandForm
from tkinter import *
from record import Record
from demo import Demo
from commands import Commands
from port import Port


def main():
    main_window = Tk()
    main_window.title("Стенд испытания шасси")
    # window.geometry('310x300')
    stand = StandForm(main_window)

    # print('Check')

    def update_loop():
        # check for demo start command
        if Port.check_port_open():
            if not Record.recording_status and not Demo.demo_running_status:
                income = Port.read_line()
                if income == Commands.start_cycle_income:
                    print('Income demo start command received')
                    stand.start_demo_button()

        # update form button status
        if not Record.recording_status and stand.record_btn_pressed:
            stand.record_button_restart()

        if not Demo.demo_running_status and stand.demo_btn_pressed:
            stand.demo_button_restart()

        main_window.after(5, update_loop)  # run again after 5ms

    main_window.after(5, update_loop)  # run first time after 5ms

    main_window.mainloop()


if __name__ == '__main__':
    main()
