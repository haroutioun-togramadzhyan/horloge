import time

def tom():
    print(time.strftime("%H:%M:%S"))
    t_am_pm = time.strftime('%I:%M:%S %p')
    print("Format anglophone(AM/PM):", t_am_pm)
    time.sleep(1)
tom()