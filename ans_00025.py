# -*- coding: utf-8 -*-
import wave 
import pyaudio
import webbrowser

from aip import AipSpeech
# 定义常量
APP_ID = '10439965'
API_KEY = 'YdA4GsfQGlHKgNjGC5zhjMmz'
SECRET_KEY = 'gqQIFMiglNqq2edNMmTSEnSyGflWR4We'

# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 8000
CHANNELS = 1
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

def record_wave():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def browser_open_text(text):

    webbrowser.get("chrome")
    str = (text[0])[:-1]
    print(str)
    if str is None:
        return
    elif 'baidu' == str:
        br = webbrowser.get("chrome")
        br = br.open("http://www.baidu.com")
        print('yes')
    elif 'google' in str or '谷歌' in str:
        br = webbrowser.get("chrome")
        br = br.open("http://www.google.com")
        print('yes')
    else:
        website = "http://www."+str+".com"
        br = webbrowser.get("chrome")
        br.open(website)
        print(website)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__ == "__main__":
    record_wave()
    res = aipSpeech.asr(get_file_content("output.wav"), 'wav', 8000, { 'lan': 'en',})
    while res['err_no'] != 0:
        print(res)
        print("Please speak again")
        record_wave()
    if 'result' in res:
        text = res['result']
        browser_open_text(text)