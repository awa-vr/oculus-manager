# Battery
- Get hmd battery: `adb shell dumpsys CompanionService | grep Battery`
- Get left controller battery: `adb shell dumpsys OVRRemoteService | grep Battery` (search for left controller)
- Get right controller battery: `adb shell dumpsys OVRRemoteService | grep Battery` (search for right controller)

# Brightness
- Get brightness: `adb shell settings get system screen_brightness`
- Set brightness: `adb shell settings put system screen_brightness <value 0-255>`

# Power levels
- Set CPU power level: `adb shell setprop debug.oculus.cpuLevel <value 0-4>`
- Set GPU power level: `adb shell setprop debug.oculus.gpuLevel <value 0-4>`