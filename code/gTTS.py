from gtts import gTTS
from tkinter import Tk
from tempfile import TemporaryFile


#tts = gTTS(text='Hello', lang='en')

#def GetClipboard():
 #   storedClipboard = Tk().clipboard_get()

from IPython.display import Audio
import time

tts = gTTS(text='Dataset successfully imported', lang='en')
f = TemporaryFile()
tts.write_to_fp(f)
f.seek(0)
Audio(f.read(), autoplay=True)
# time.sleep(5) # doesn't work to avoid the file to close to fast...
# f.close() # ... this has to be in the next cell otherwise the sound is not played

#! attempting ways to automatically play and delete the created mp3 file
#! so far nothing is working