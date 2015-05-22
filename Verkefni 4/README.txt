CleanUP

Requirements:
Python
external packaged used are guessit wich again uses stevedore and babelfish. 
All are included and a small hack was added at the head of cleanup.py so there
should be no need for TA's to install them outside of the directory cleanup.py
is run from.

HowTo:
1. run cleanup.py
2. enter the absolute path to the directory (or drag the folder to commandline)
i.e. 'C:\Users\Kalli\Desktop\Verkefni4\downloads'
3. Magic

Goes through the folder and sorts content into folders based on results from guessit.
First it checks folders. Then files.
Unrecongized folders are placed in a folder called VariousUnsorted. This is done so not 
to mess with folder structure of tv shows/music that are already sorted but not recongized by 
guessit.

Sorts tv shows into TvShows Folder and movies into Movies folder.

It then sweeps the root one more time and check for leftover files not contained in a folder
or recognized by guessit and sorts into folders according to extension.

deletes empty folders.

arniola12@ru.is
karl12@ru.is
