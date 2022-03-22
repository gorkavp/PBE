import binascii
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C


class RfidPN532:
    def read_uid(self):
        reset_pin = DigitalInOut(borad.D6)
        req_pin = DigitalInOut(board.D12)
        i2c = busio.I2C(i2c, , debug=False, reset=reset_pin, req=req_pin)
        pn532.SAM_configuration()
        if (not pn532.firmware_version):
            print("Error de conexión")
        ledio = False
        while leido == False:
            uid = pn532.read_passive_target(timeout=0.5)
            if uid is None:
                continue
            leido = True
            uid = binsascii.hexlify(uid).decode('utf-8').upper()
        return uid


if __name__ == "__main__":
    rf = RfidPN532()
    print("Acerque su targeta al lector")
    uid = rf.read_uid()
    print("La UID detectada es" + uid)
