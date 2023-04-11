# Battery
- Get hmd: `adb shell dumpsys CompanionService | grep Battery`
- Get left controller: `adb shell dumpsys OVRRemoteService | grep Battery` (search for left controller)
- Get right controller: `adb shell dumpsys OVRRemoteService | grep Battery` (search for right controller)

# Bitrate
- Set Bitrate: `adb shellsetprop debug.oculus.capture.bitrate <value>`
- Values:
    - 5mbps: `5000000`
    - 10mbps: `10000000`
    - 15mbps: `15000000`
    - 20mbps: `20000000`

# Brightness
- Get: `adb shell settings get system screen_brightness`
- Set: `adb shell settings put system screen_brightness <value 0-255>`

# Video capture res
- Set width: `adb shell setprop debug.oculus.capture.width <width>`
- Set height: `adb shell setprop debug.oculus.capture.height <height>`
- Values:
    - 640x480
    - 1280x720
    - 1920x1080
    - 1024x1024 (default)
    - 1600x1600

# FFR
- Set: `adb shell debug.oculus.foveation.level <value>`
- Values:
    - off: `0`
    - low: `1`
    - medium: `2`
    - high: `3`
    - max: `4`

# Recording fps
- Set: `adb shell setprop debug.oculus.capture.fps <value>`
- Values:
    - 24fps: `24`
    - 30fps: `30`
    - 60fps: `60`

# Install apk
- `adb install <path_to_apk>` 

# Power levels
- Set CPU: `adb shell setprop debug.oculus.cpuLevel <value 0-4>`
- Set GPU: `adb shell setprop debug.oculus.gpuLevel <value 0-4>`

# Refresh rate
- Set: `adb shell setprop debug.oculus.refreshRate <value>`
    - Values:
        - 72
        - 80
        - 90
        - 120
- Get: `adb shell getprop debug.oculus.refreshRate`

# Texture res
- Set width: `adb shell setprop debug.oculus.textureWidth <width>`
    - Values:
        - default: `1440`
        - 512: `512`
        - 768: `768`
        - 1024: `1024`
        - 1280: `1280`
        - 1440: `1440`
        - 1536: `1536`
        - 2048: `2048`
        - 2560: `2560`
        - 3072: `3072`
- Set height: `adb shell setprop debug.oculus.textureHeight <height>`
    - Values:
        - default: `1584`
        - 512: `563`
        - 768: `845`
        - 1024: `1127`
        - 1280: `1408`
        - 1440: `1584`
        - 1536: `1690`
        - 2048: `2253`
        - 2560: `2816`
        - 3072: `3380`

# Proximity sensor
- Enable: `adb shell am broadcast -a com.oculus.vrpowermanager.automation_disable`
- Disable: `adb shell am broadcast -a com.oculus.vrpowermanager.prox_close`

# Guardian
- Enable: `adb shell setprop debug.oculus.guardian_pause 1`
- Disable: `adb shell setprop debug.oculus.guardian_pause 0`

# Chroma
- Enable: `adb shell setprop debug.oculus.forceChroma 1`
- Disable: `adb shell setprop debug.oculus.forceChroma 0`

# Experimental features
- Enable: `adb shell setprop debug.oculus.experimentalEnabled 1`
- Disable: `adb shell setprop debug.oculus.experimentalEnabled 0`

# Dynamic FFR
- Enable: `adb shell setprop debug.oculus.foveation.dynamic 1`
- Disable: `adb shell setprop debug.oculus.foveation.dynamic 0`