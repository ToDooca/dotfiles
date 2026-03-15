#!/usr/bin/env python3
# Run: python3 ~/.config/qtile/scripts/debug_openrazer.py

try:
    from openrazer.client import DeviceManager
    dm = DeviceManager()
    print("OpenRazer import OK. Devices found:", len(dm.devices))
    for i, d in enumerate(dm.devices):
        name = getattr(d, 'name', '?')
        bl = getattr(d, 'battery_level', 'N/A')
        ch = getattr(d, 'is_charging', 'N/A')
        print(f"  [{i}] name={name!r} battery_level={bl} is_charging={ch}")
except Exception as e:
    print("OpenRazer error:", type(e).__name__, e)
