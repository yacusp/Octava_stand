# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from win_form import StandForm
from tkinter import *
from record import Record
from port import Port

def main():

    main_window = Tk()
    main_window.title("Стенд испытания шасси")
    #window.geometry('310x300')
    stand = StandForm(main_window)
    #print('Check')

    def update_loop():
        if Port.connected_status:
            if not Record.recording_status:
                print('Not recording')
                income = Port.read_command()
                print(income)
            print('Update!')
            #income = stand.new_port.read_command()

        main_window.after(5, update_loop)  # run again after 5ms

    main_window.after(5, update_loop)  # run first time after 5ms

    main_window.mainloop()


if __name__ == '__main__':
    main()
