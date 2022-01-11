from crc import crc8


def us_to_ticks(pwm_values):
    ticks_list = []
    for pwm in pwm_values:
        tick = (pwm-1500)*(1.6) + 992
        ticks_list.append(int(tick))
    return ticks_list

def ticks_to_us(ticks_values):
    pwm_list = []
    for ticks in ticks_values:
        pwm = (ticks-992)*(5/8) + 1500
        pwm_list.append(int(pwm))
    return pwm_list

def pack_channels(channel_data):
    # channel data: array of 16 integers
    channel_data = list(reversed(channel_data))
    pack_bit = []
    for idx, channel in enumerate(channel_data):
        pack_bit[idx*11: (idx+1)*11] = "{0:011b}".format(channel)
    pack_bit=''.join(pack_bit)
    pack_byte = []
    for idx in range(22):
        current_byte = int(pack_bit[idx*8:(idx+1)*8], 2)
        pack_byte.append(current_byte)
    pack_byte = list(reversed(pack_byte))
    return pack_byte

def crc_transmit(type, payload):
    h = crc8()
    h.update(bytearray(type + payload))
    return h.hexdigest()

# a = crc_transmit([16], [232 ,131 ,37 ,250 ,184 ,139 ,62 ,244 ,161 ,15 ,125 ,232 ,67 ,31 ,119 ,185 ,203 ,93 ,238 ,114 ,151 ,187])
# print(a)