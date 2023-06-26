# Audio file formats
# .mp3 - compresses data, could lose information
# .flac - lossless information, also compresses data
# .wav - uncompressed format, audio quality is the best but file size largest

import wave

# Audio signal parameters
# - number of channels
# - sample width
# - framerate/sample_rate: 44,100 Hz
# - number of frames
# - values of a frame

obj = wave.open("01-basics_output.wav", "rb") #read binary mode

print("Number of channels", obj.getnchannels())
print("Sample Width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

obj_new = wave.open("anmol_new.wave", "wb") #write binary mode

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()


