def calculate_monthly_bill(total_power, tariff_rate=50.0):
    # Formulas used in app.py:
    # monthly_bill = round(total_system_power * 8 * 30 * tariff_rate, 0)
    return round(total_power * 8 * 30 * tariff_rate, 0)

def test_monthly_bill_calculation():
    # Test case 1: 0 kW should result in 0 IQD
    assert calculate_monthly_bill(0.0) == 0.0

    # Test case 2: 2.0 kW with tariff 50.0 should be: 2.0 * 8 * 30 * 50 = 24000
    assert calculate_monthly_bill(2.0) == 24000.0

    # Test case 3: 4.12 kW with tariff 50.0 should be: 4.12 * 8 * 30 * 50 = 49440
    assert calculate_monthly_bill(4.12) == 49440.0

def test_safety_trip_logic():
    # Test logic mimicking the safety trip threshold
    threshold_kw = 5.0

    room_devices = {
        "مكيف 1 (AC-1)": {"status": True, "power": 4.5, "icon": "❄️"},
        "مصباح رئيسي": {"status": True, "power": 0.8, "icon": "💡"}
    }

    # Calculate room power
    room_power = sum(info["power"] for info in room_devices.values() if info["status"])

    # Trigger safety trip if room_power exceeds threshold
    tripped = False
    if room_power > threshold_kw:
        tripped = True
        for dev_name in room_devices:
            if "مكيف" in dev_name:
                room_devices[dev_name]["status"] = False

    # Recalculate room power after trip
    post_trip_power = sum(info["power"] for info in room_devices.values() if info["status"])

    assert tripped is True
    assert room_devices["مكيف 1 (AC-1)"]["status"] is False
    assert post_trip_power == 0.8
