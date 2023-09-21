"""Ping"""
def main():
    """Ping!!!!"""
    ping = input()
    ping = input()
    ping = input()
    pack1 = input()
    pack2 = input()
    pack3 = input()
    pack4 = input()
    received = 0
    average = 0
    val_min = 9999999
    val_max = 0

    if '[' in ping:
        ip_ = ping[ping.find('[')+1:ping.find(']')] + ':'
    else:
        ip_ = ping[ping.find(' ')+1:ping.find('with')-1] + ':'
    if ip_ in pack1:
        received += 1
        time_ = time(pack1)
        if pack1[pack1.find('time')+4:pack1.find('time')+6] == '<1':
            time_ = 0
        average += time_
        val_max = time_
        val_min = time_
    if ip_ in pack2:
        received += 1
        time_ = time(pack2)
        if pack2[pack2.find('time')+4:pack2.find('time')+6] == '<1':
            time_ = 0
        average += time_
        val_max = check_max(val_max, time_)
        val_min = check_min(val_min, time_)
    if ip_ in pack3:
        received += 1
        time_ = time(pack3)
        if pack3[pack3.find('time')+4:pack3.find('time')+6] == '<1':
            time_ = 0
        average += time_
        val_max = check_max(val_max, time_)
        val_min = check_min(val_min, time_)
    if ip_ in pack4:
        received += 1
        time_ = time(pack4)
        if pack4[pack4.find('time')+4:pack4.find('time')+6] == '<1':
            time_ = 0
        average += time_
        val_max = check_max(val_max, time_)
        val_min = check_min(val_min, time_)

    #print
    printt(received, ip_, val_min, val_max, average)

def printt(received, ip_, val_min, val_max, average):
    """print"""
    print('Ping statistics for', ip_)
    print('    Packets: Sent = 4, Received = %d, Lost = %d (%d%s loss),'\
        % (received, 4-received, (4-received)*25, '%'))
    if received != 0:
        print('Approximate round trip times in milli-seconds:')
        print('    Minimum = %dms, Maximum = %dms, Average = %dms'\
            % (val_min, val_max, average//received))

def check_max(val1, val2):
    """find max"""
    if val1 > val2:
        return val1
    return val2

def check_min(val1, val2):
    """find min"""
    if val1 < val2:
        return val1
    return val2

def time(val):
    """time"""
    return int(val[val.find('time')+5:val.find('ms')])
main()
