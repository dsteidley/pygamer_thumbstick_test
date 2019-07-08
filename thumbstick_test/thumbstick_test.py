import board
import analogio
import time

adc = analogio.AnalogIn(board.JOYSTICK_X)

polarity = -1
scale = .0625
offset = 2056
sample_count = 10

read_as_digital = 1
x_null = 1000

if not read_as_digital:
    while True:
        x_buffer = 0.0
        for i in range(0,sample_count):
            x_buffer = x_buffer + adc.value
            time.sleep(0.01)
        x_avg = x_buffer / sample_count
        x_val = (x_avg * polarity * scale) + offset
        print((x_val,))
        time.sleep(0.1)
else:
    while True:
        x_buffer = (adc.value * polarity * scale) + offset
        if x_buffer > x_null:
            x_val = 1
        elif x_buffer < x_null * -1:
            x_val = -1
        else:
            x_val = 0
        print((x_val,))
        time.sleep(0.1)