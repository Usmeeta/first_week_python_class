batteries = [50, 30, 4, 45, 12, 18, 30]  ## battery basket
minimum_battery_power = 20  ## battery use minimum 20% charge
usable_battery_power = 0   ## battery 0 power 0
usable_battery_count = 0   ## usable battery 0
for battery in batteries:  ## check every battery
    if battery > minimum_battery_power:   
        usable_battery_power += battery
        usable_battery_count = usable_battery_count + 1

print(usable_battery_power, usable_battery_count)
