import time
import os

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")
    os.system("say 'Time is up!'")  # 在macOS上使用系统语音播放提示音

# 设置专注时间（以分钟为单位）
focus_time = 25

countdown(focus_time)
