from classtest import *
import threading
import time
from pynput import keyboard

profiles = [ProfileInfo('Thread 1'), ProfileInfo('Thread 2')]
listen = keyboard.Listener


def showInfo(profile, sleep_time):
    while True:
        if (profile.isStop):
            print("{} Stop\n".format(profile.Name))
            break

        print("Profile: {} - again after {}\n".format(profile.Name, sleep_time))
        time.sleep(sleep_time)

        if (profile.isStop):
            print("{} Stop\n".format(profile.Name))
            break

    total_running_thread = any(x.isStop==False for x in profiles)
    print("Total: {}\n".format(total_running_thread))

    if(total_running_thread==False):
        listen.stop()

def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    print("vk =", vk)

    if(vk==None):
        return 
    index = vk-48

    if(index>=0 and index<len(profiles) and profiles[index].isStop==False):
        print("Doing stop: {}".format(profiles[index].Name))
        profiles[index].isStop = True

if __name__ == "__main__":
    for item in profiles:
        p =threading.Thread(target=showInfo, args=(item, 1))
        p.start()

    with keyboard.Listener(on_press=on_press) as listener:
        listen = listener
        listener.join()
  

