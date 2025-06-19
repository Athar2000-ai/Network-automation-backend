import yaml
import os
import platform
from getpass import getpass
# from netmiko import ConnectHandler  # Uncomment when running with actual devices

def load_devices(group_name):
    with open("devices.yaml") as f:
        data = yaml.safe_load(f)
    return data["groups"].get(group_name, [])

def is_reachable(ip):
    ping_cmd = "ping -n 1" if platform.system().lower() == "windows" else "ping -c 1"
    response = os.system(f"{ping_cmd} {ip} > /dev/null 2>&1")
    return response == 0

def connect_and_run(device):
    ip = device["ip"]
    if is_reachable(ip):
        print(f"[{ip}] ✅ Reachable. Attempting SSH...")

        # Uncomment the following block to enable SSH
        """
        try:
            connection = ConnectHandler(**device)
            connection.enable()
            output = connection.send_command("show version")
            print(f"[{ip}] ✅ Connected")
            print(output)
            connection.disconnect()
        except Exception as e:
            print(f"[{ip}] ❌ SSH Error: {e}")
        """
        print(f"[{ip}] 🔐 (SSH logic is currently commented out)")
    else:
        print(f"[{ip}] ❌ Unreachable")

if __name__ == "__main__":
    group = input("Enter device group (e.g., access_switches, core_routers): ").strip()
    devices = load_devices(group)

    if not devices:
        print(f"No devices found in group: {group}")
    else:
        for device in devices:
            connect_and_run(device)
