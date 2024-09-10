import os
import sys
from downloader import Downloader
from view import View

# determine if application is a script file or frozen exe + using absolute path (relative doenst work for .exe files)
if getattr(sys, 'frozen', False):
    path_to_root = os.path.dirname(sys.executable)
elif __file__:
    path_to_root = os.path.split(os.path.dirname(__file__))[0]
        
output_path = os.path.join(path_to_root, "Output")
ffmpeg_path=  os.path.join(path_to_root, r"ffmpeg.exe")
sources_path = os.path.join(path_to_root, "Sources")

downloader = Downloader(output_path, ffmpeg_path)

view = View(downloader, sources_path)

view.start()

# TODO 
    #progressbar
    #richtige codecs für itunes 
        #ffmpeg -i input.mov -vcodec hevc_videotoolbox -b:v 6000k -tag:v hvc1 -c:a eac3 -b:a 224k output.mov        erkennt itunes, aber als video
        #ffmpeg -i video.mp4 -c:v mpeg4 -c:a aac full_mpeg4_aac.mp4   works, but video hasnt good resolution
        #ffmpeg -i video.mp4 -c:v libx264 -c:a aac full_h.264_aac.mp4

    #ffmpeg mit Meldung "Changing Codecs..." implementieren
    #file names anpassen (z.B. wird schonvorhandener audio file bei downloadd all gelöscht)

# bsp. video: https://www.youtube.com/watch?v=cHm5qM5voXQ
# weniger lang: https://www.youtube.com/watch?v=fQPahy5LI_8&pp=ygUUdmlkZW8gbm90IG11Y2ggZGlzayA%3D
# Pennymarkt: https://www.youtube.com/watch?v=G_4AxeLYR8A&t=13s&pp=ygUQcGVubnkgbWFya3QgZG9rdQ%3D%3D
# dollarzeichen im namen: https://youtu.be/gtdejuLP2hw

#sys.stdout.write = self.redirector #whenever sys.stdout.write is called, redirector is called.
#def redirector(self,inputStr):
    #self.log.insert(tk.END, inputStr)