# NeoSmartBlue Python Library

A Python library for controlling Neo Smart Blinds via BlueLink Bluetooth connection.

## Installation

```bash
pip install neosmartblue-py
```

## Usage

### Scanning for devices and reading status from advertisements

```python
import asyncio
from neosmartblue.py import scan_for_devices

async def main():
    # Scan for nearby Neo Smart Blinds devices
    devices = await scan_for_devices(timeout=5.0)
    
    for device in devices:
        print(f"Found device: {device['name']} ({device['address']})")
        print(f"  Position: {device['status']['current_position']}%")
        print(f"  Battery: {device['status']['battery_level']}%")
        print(f"  Moving: {'Yes' if device['status']['is_moving'] else 'No'}")

asyncio.run(main())
```

### Controlling a device

```python
import asyncio
from neosmartblue.py import BlueLinkDevice

async def main():
    # Replace with your device's MAC address
    device = BlueLinkDevice("XX:XX:XX:XX:XX:XX")
    
    # Connect to the device
    await device.connect()
    
    try:
        # Move blinds to 50% closed position
        await device.move_to_position(50)
        
        # Stop movement if needed
        # await device.stop()
    
    finally:
        # Disconnect from device
        await device.disconnect()

asyncio.run(main())
```