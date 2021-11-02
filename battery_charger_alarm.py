import androidhelper
import time
import sys


def battery_check():
    battery_level = droid.batteryGetLevel().result

    status_values = {1:"Unknown", 2:"Charging", 3:"Discharging", 4:"Not Charging", 5:"Full"}
    battery_status = droid.batteryGetStatus().result

    health_values = {1:"Unknown", 2:"Good", 3:"Overheat", 4:"Dead", 5:"Over Voltage", 6:"Unspecified Failure"}
    battery_health = droid.batteryGetHealth().result
    
    return [f"Charge Level: {battery_level} %\n\rBattery Status: {status_values[battery_status]}\n\rBattery Health: {health_values[battery_health]}", 
            battery_level, status_values[battery_status]]

def start_alarm():
    droid.mediaPlay(r"/storage/emulated/0/qpython/scripts3/mv.mp3")
    droid.dialogCreateAlert('Alarm', 'Press Button Stop To Exit!!')
    droid.dialogSetPositiveButtonText(" Stop ")
    droid.dialogShow()
    response = droid.dialogGetResponse().result
    droid.dialogDismiss()

def check_every_30sec(start_battery_level):
    current_battery_level = battery_check()[1]
    while True:
        if current_battery_level >= 95 or (current_battery_level + start_battery_level) == 100:
            print(battery_check()[0])
            droid.ttsSpeak(f'Your battery level now is {current_battery_level}%, please disconnect the charger')
            time.sleep(5)
            start_alarm()
            break
        else:
            time.sleep(30)
            current_battery_level = battery_check()[1]
            print(battery_check()[2])


# Start of main program
try:
    droid = androidhelper.Android()
    droid.batteryStartMonitoring()

    start_battery_level = battery_check()[1]
    print(f'Your battery start level  is {start_battery_level}%')
    droid.ttsSpeak(f'Your battery start level  is {start_battery_level}%')

    check_every_30sec(start_battery_level)
except:
    droid.ttsSpeak(f'sorry, there is a problem with the program')
finally:
    droid.batteryStopMonitoring()
    droid.mediaPlayClose()
    sys.exit(0)


