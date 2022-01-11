
from com import communication
import time
import csv
import threading


# initialize serial communication
com = communication(com_port='/dev/ttyUSB0')

# initialize thread
thread = threading.Thread(target=com.transmit, daemon=True)
thread.start()

thread2 = threading.Thread(target=com.decode_telemetry, daemon=True)
thread2.start()

# disarming channels
disarm_channels = [1500, 1500, 885, 1500, 1000, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
com.update_data(disarm_channels)
time.sleep(2)

# arming channels
arm_channels = [1500, 1500, 885, 1500, 1800, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
com.update_data(arm_channels)
time.sleep(2)

# csv settings
csv_counter = 0
dicts = []
save_after = 100000  # seconds
t1 = time.time()

while True:
    channels_pwm = [1500, 1500, 1050, 1500, 1800, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
    com.update_data(channels_pwm)
    data = {'time': time.time(), 'throttle': channels_pwm[2]}
    dicts.append(data)
    time.sleep(0.01)

    channels_pwm = [1500, 1500, 1500, 1500, 1800, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
    com.update_data(channels_pwm)
    data = {'time': time.time(), 'throttle': channels_pwm[2]}
    dicts.append(data)
    time.sleep(0.01)

    if (time.time()-t1) > save_after:
        print("saving csv file")
        com.update_data(disarm_channels)
        keys = dicts[0].keys()

        with open('command_data.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(dicts)

