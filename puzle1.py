import binascii
import board
import busio
from adafruit_pn532.i2c import PN532_I2C


class RfidPN532:

    def __init__(self):
        self.pn532 = PN532_I2C(busio.I2C(board.SCL, board.SDA))

    def read_uid(self):
        self.pn532.SAM_configuration()
        uid = None
        while uid == None:
            uid = self.pn532.read_passive_target(timeout=0.5)
        return binascii.hexlify(uid).decode('utf-8').upper()


if __name__ == "__main__":
    rf = RfidPN532()
    print("Acerque su targeta al lector")
    uid = rf.read_uid()
    print("La UID detectada es " + uid)
