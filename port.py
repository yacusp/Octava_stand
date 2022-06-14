import sys
import glob
import serial


class Port:
    speeds = [115200, 57600, 9600]
    speed = speeds[0]
    port_name = 'COM1'
    connection = serial.Serial()
    connected_status = False

    @staticmethod
    def serial_ports():
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        if len(result) > 0:
            return result
        else:
            return [0]


    @classmethod
    def set_speed(cls, new_speed):
        cls.speed = int(new_speed)

    @classmethod
    def set_port(cls, new_port):
        cls.port_name = new_port

    @classmethod
    def connect(cls):
        cls.connection = serial.Serial(cls.port_name, cls.speed)
        cls.connected_status = True

    @classmethod
    def disconnect(cls):
        cls.connection.close()
        cls.connected_status = False

    @classmethod
    def send_line(cls, command):
        if cls.connection:
            cls.connection.write(command)

    @classmethod
    def read_line(cls):
        if cls.connection.inWaiting() > 0:
            return cls.connection.readline().decode('utf-8')

    @classmethod
    def check_port_open(cls):
        if cls.connection.isOpen():
            return True
        else:
            cls.connected_status = False
            return False
