# -*- coding: utf-8 -*-					#編碼格式
import pyaudio
import sys
import numpy as np
import wave
import audioop
import struct

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
    
p = pyaudio.PyAudio()
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = chunk)
swidth = 2
count = 0
num = int(input('What pitch '))				#輸入想要轉換的聲調
print ("* recording")
while True:
    try:							#try-except 當遇到錯誤即跳過
        if count == 1024:					#當執行1024次後會給一次停止判斷
            x = input('Do you want to continue ? If yes, please enter 1 ')
            if x == 1:
                count = 0
                print(count)
                continue
            else:
                break

        data = stream.read(chunk)
        data = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data))/2 
        data = np.fft.rfft(data)					#進行傅立葉轉換
        new_fft = np.roll(data,num*2)				#shift以進行音調變換
        if num>0:
              for i in range(0, num*2):
                    data[i] = 0
          else:
              for i in range(len(data)-num*2,len(data)-1):
                data[i] = 0
        data = np.fft.irfft(new_fft)					#反轉換
        dataout = np.array(data, dtype='int16')
        chunkout = struct.pack("%dh"%(len(dataout)), *list(dataout)) 
        stream.write(chunkout)

        count=count+1
        print(count)

    except:
        pass
        print("error")

print ("* done")
stream.stop_stream()
stream.close()
p.terminate()
