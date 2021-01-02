def collect_audio(filePath='output.wav'):
    import pyaudio
    import math
    import struct
    import wave
    import time
    import os


    Threshold = 10

    SHORT_NORMALIZE = (1.0/32768.0)
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    swidth = 2

    TIMEOUT_LENGTH = 1

    f_name_directory = r''

    class Recorder:

        @staticmethod
        def rms(frame):
            count = len(frame) / swidth
            format = "%dh" % (count)
            shorts = struct.unpack(format, frame)

            sum_squares = 0.0
            for sample in shorts:
                n = sample * SHORT_NORMALIZE
                sum_squares += n * n
            rms = math.pow(sum_squares / count, 0.5)

            return rms * 1000

        def __init__(self):
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      input=True,
                                      output=True,
                                      frames_per_buffer=chunk)

        def record(self, filePath):
            print('\tnoise detected, recording beginning')
            rec = []
            current = time.time()
            end = time.time() + TIMEOUT_LENGTH

            while current <= end:

                data = self.stream.read(chunk)
                if self.rms(data) >= Threshold: end = time.time() + TIMEOUT_LENGTH

                current = time.time()
                rec.append(data)
            self.write(b''.join(rec))

        def write(self, recording):

            filename = os.path.join(f_name_directory, filePath)

            wf = wave.open(filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(recording)
            wf.close()
            # print('\twritten to file: {}'.format(filename))



        def listen(self):
            print('listening...')
            has_recorded = False
            while has_recorded is False:
                input = self.stream.read(chunk)
                rms_val = self.rms(input)
                if rms_val > Threshold:
                    self.record(filePath)
                    has_recorded = True

    a = Recorder()

    a.listen()

    return("OK")

def analyze_audio(str_chinese
                , str_pinyin
                , str_english
                ,filePath='output.wav'
                , exFilePath='output.wav'):

    import parselmouth
    import numpy as np

    import matplotlib.font_manager as mfm
    import matplotlib.pyplot as plt

    font_path = 'New Song (Ming) Typeface (Heiti TC Light) Font-Simplified Chinese.ttf'
    prop = mfm.FontProperties(fname=font_path)

    snd = parselmouth.Sound(f"{filePath}")
    exSnd = parselmouth.Sound(f"{exFilePath}")

    fig, axes = plt.subplots(ncols=1, nrows=3)

    userColor = 'blue'
    exColor = 'red'

    ### Plot sound
    axes[0].plot(snd.xs(), snd.values.T, color=userColor, alpha=0.5)
    axes[0].plot(exSnd.xs(), exSnd.values.T, color=exColor, alpha=0.5)
    axes[0].set_xlim([min(snd.xmin, exSnd.xmin), max(snd.xmax, exSnd.xmax)])
    axes[0].set_xlabel('time [sec]')
    axes[0].set_ylabel('amplitude')


    ### Plot pitch
    pitch = snd.to_pitch()
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values == 0] = np.nan
    axes[1].plot(pitch.xs(), pitch_values, 'o', markersize=2, color=userColor)

    pitch = exSnd.to_pitch()
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values == 0] = np.nan
    axes[1].plot(pitch.xs(), pitch_values, 'o', markersize=2, color=exColor)

    axes[1].set_ylim(0, pitch.ceiling)
    axes[1].set_ylabel("fundamental\nfrequency [Hz]")

    ### Plot intensity
    intensity = snd.to_intensity()
    axes[2].plot(intensity.xs(), intensity.values.T, linewidth=1, color=userColor)

    intensity = exSnd.to_intensity()
    axes[2].plot(intensity.xs(), intensity.values.T, linewidth=1, color=exColor)

    axes[2].set_ylim(0)
    axes[2].set_ylabel("intensity [dB]")

    plt.tight_layout()
    plt.savefig("plot.png")
    
def retrieve_example_audio(exFilePath, text, lang='en'):
    from google_speech import Speech

    speech = Speech(text, lang)
    # save the speech to an MP3 file (no effect is applied)
    speech.save(exFilePath)
    


def collect_user_speech_button_press():
    
    # Google Translate API started having issues in late 2020; just assume a sentence is given 
    str_chinese = "因为所以可携大力国家机密不能告你!"
    str_pinyin = "Yīn wéi suǒyǐ kě xī dàlì guójiā jīmì bùnéng gào nǐ!"
    str_english = "translation"

    collect_audio()

    # Automatically trigger : retrieve example audio 
    retrieve_example_audio(
        exFilePath='example.wav',
        text=str_chinese,
        lang='zh'
    )

    # Plot analysis 
    analyze_audio(
        filePath='example.wav',
        exFilePath='output.wav',
        str_chinese='ch',
        str_pinyin='pinyin',
        str_english='en'
    )

collect_user_speech_button_press()
