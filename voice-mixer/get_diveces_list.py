from pycaw.pycaw import AudioUtilities

sound_speakers = AudioUtilities.GetSpeakers()
print(sound_speakers)
all_devices = AudioUtilities.GetAllSessions()
print(all_devices)
# devices = AudioUtilities.GetAllDevices()
# volume = devices.EndpointVolume


#  volume.SetMute(1, None)
