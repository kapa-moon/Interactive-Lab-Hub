# !/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import argparse
import queue
import sys
import sounddevice as sd
import json 
from vosk import Model, KaldiRecognizer
import time
q = queue.Queue()

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))
    
    
class SpeechRecognizer: 
    def __init__(self):
        self.parser = argparse.ArgumentParser(add_help=False)
        self.parser.add_argument(
            "-l", "--list-devices", action="store_true",
            help="show list of audio devices and exit")
        args, remaining = self.parser.parse_known_args()
        if args.list_devices:
            print(sd.query_devices())
            self.parser.exit(0)
        self.parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[self.parser])
        self.parser.add_argument(
            "-f", "--filename", type=str, metavar="FILENAME",
            help="audio file to store recording to")
        self.parser.add_argument(
            "-d", "--device", type=int_or_str,
            help="input device (numeric ID or substring)")
        self.parser.add_argument(
            "-r", "--samplerate", type=int, help="sampling rate")
        self.parser.add_argument(
            "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
        self.args = self.parser.parse_args(remaining)
        
        if self.args.samplerate is None:
            device_info = sd.query_devices(self.args.device, "input")
            # soundfile expects an int, sounddevice provides a float:
            self.args.samplerate = int(device_info["default_samplerate"])
            
        if self.args.model is None:
            self.model = Model(lang="en-us")
        else:
            self.model = Model(lang=self.args.model)

        if self.args.filename:
            self.dump_fn = open(self.args.filename, "wb")
        else:
            self.dump_fn = None

    def getStream(self):
        stream = sd.RawInputStream(samplerate=self.args.samplerate, blocksize = 8000, device=self.args.device,
                    dtype="int16", channels=1, callback=callback)
        
        return stream
        
    def getTranscript(self, writeToScreen, button):
        last_text = ""
        stream = self.getStream()        

        rec = KaldiRecognizer(self.model, self.args.samplerate)

        try:            
            with stream:
                print("#" * 80)
                print("Press Ctrl+C to stop the recording")
                print("#" * 80)


                
                # count_button = 0
                
                while True:
                    if button.is_button_pressed():
                        print("Button is pressed!")
                        break

                    # if button.is_button_pressed():
                    #     count_button += 1
                        
                    # if (count_button > 1):
                    #     break
                        
                    data = q.get()
                    if rec.AcceptWaveform(data):
                        rec_dict = json.loads(rec.Result())
                        
                        last_text = rec_dict['text']
                        writeToScreen(rec_dict['text'])
                    # else:
                    #     print(rec.PartialResult())
                    if self.dump_fn is not None:
                        self.dump_fn.write(data)
                    
                print("The loop is stopped 100%")
        
        except KeyboardInterrupt:
            print("\nDone")
            self.parser.exit(0)
        except Exception as e:
            self.parser.exit(type(e).__name__ + ": " + str(e))
            
        return last_text


# speechRecognizer = SpeechRecognizer()
# speechRecognizer.getTranscript()