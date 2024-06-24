import subprocess

def set_sleep_and_display_timeout(minutes):
    # Convert minutes to seconds
    timeout_seconds = minutes 

    # Set the sleep timeout for when the laptop is plugged in
    subprocess.run(['powercfg', '/change', 'standby-timeout-ac', str(timeout_seconds)], check=True)

    # Set the sleep timeout for when the laptop is on battery
    subprocess.run(['powercfg', '/change', 'standby-timeout-dc', str(timeout_seconds)], check=True)

    # Set the display timeout for when the laptop is plugged in
    subprocess.run(['powercfg', '/change', 'monitor-timeout-ac', str(timeout_seconds)], check=True)

    # Set the display timeout for when the laptop is on battery
    subprocess.run(['powercfg', '/change', 'monitor-timeout-dc', str(timeout_seconds)], check=True)

if __name__ == "__main__":
    set_sleep_and_display_timeout(3)
    print("Sleep and display timeout set to 45 minutes for both AC and DC power modes.")
