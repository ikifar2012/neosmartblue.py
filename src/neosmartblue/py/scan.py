import asyncio
from typing import Dict, List, Optional, Any
from bleak import BleakScanner

from .parse_status import parse_status_data

async def scan_for_devices(timeout: float = 5.0) -> List[Dict[str, Any]]:
    """
    Scan for Neo Smart Blinds devices and return their advertisement data.
    
    Parameters:
        timeout (float): The number of seconds to scan for devices.
        
    Returns:
        List[Dict[str, Any]]: List of discovered devices with their status information.
    """
    devices = []
    
    def detection_callback(device, advertisement_data):
        # Check if this is a Neo Smart Blinds device
        if device.name and "NEO" in device.name.upper():
            # Get manufacturer data if available
            if advertisement_data.manufacturer_data:
                for company_id, data in advertisement_data.manufacturer_data.items():
                    if len(data) >= 7:  # Ensure enough data for status parsing
                        try:
                            status = parse_status_data(data)
                            devices.append({
                                "address": device.address,
                                "name": device.name,
                                "rssi": device.rssi,
                                "status": status,
                                "raw_data": data.hex().upper(),
                            })
                        except Exception as e:
                            print(f"Failed to parse status for {device.address}: {e}")
    
    scanner = BleakScanner(detection_callback=detection_callback)
    await scanner.start()
    await asyncio.sleep(timeout)
    await scanner.stop()
    
    return devices