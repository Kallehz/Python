import os
import sys
import shutil
#needed to use local packages fixes py3 import error for tvname
#to use local modules...
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
#secondary dependencies. Present in folder and imported here preemptively so TA does not need to install them. 
import stevedore
import babelfish
# GUESSIT. Only dependency actually used by us.
from guessit import guess_file_info


#constanst
extensList = ['avi', 'AVI', 'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv','mpg', 'mpeg', 'm2v', 'wmv', 'mov','qt', 'mkv', 'webm', 'vob', 'srt']
extensToDelete = ['txt', 'nfo', 'dat', 'ini', 'jpg', 'torrent']
	
def checkFiles(root):
	'''
	Fakes in path to folder and attempts to to sort files according to type.
	'''
	excludedDirs = ['TvShows', 'Movies', 'VariousUnsorted']	
	for folderName, subfolders, filenames in os.walk(root, topdown=True):
		subfolders[:] = [d for d in subfolders if d not in excludedDirs]
		
		for filename in filenames:
			thefile = os.path.join(folderName, filename)
			extension = thefile.split(".")[-1]
			if extension in extensList:
				if extension[0] is 'r':
					extension = 'rar'
				if extension != 'DS_Store':
					guessVideoType(thefile)
			if	extension in extensToDelete:
				os.remove(thefile)
		for folder in subfolders:
			fold = os.path.join(folderName, folder)
			guessVideoType(fold)


def guessVideoType(videofile):
	'''
	Takes in a path to videofile and takes a guesses at what the videofile contains and moves acordingly.
	Not perfect. At all.
	'''
	guess = guess_file_info(videofile, info=['filename'])
	if guess['type'] is 'episode':
		try:
			path = os.path.join('TvShows' , guess['series'], 'season '+str(guess['season']))
			if  os.path.exists(path):
				shutil.move(videofile, path)
			else:
				os.makedirs(path)
				shutil.move(videofile, path)
		except Exception as e:
			pass
	elif guess['type'] is 'movie':
		try:
			path = os.path.join('Movies')
			if  os.path.exists(path):
				shutil.move(videofile, path)
			else:
				os.makedirs(path)
				shutil.move(videofile, path)
		except Exception as e:
				pass
	else:
		try:
			path = os.path.join('VariousUnsorted')
			if  os.path.exists(path):
				shutil.move(videofile, path)
			else:
				os.makedirs(path)
				shutil.move(videofile, path)
		except Exception as e:
				pass

	
def sortLeftovers(root):
	'''
	Takes in path to folder and sorts according to file ending.
	Does not goe through folders called 'TvShows', 'Movies', 'VariousUnsorted' assuming they were made by other sorting functions.
	If file is present when trying to move it should be renamed.
	'''
	excludedDirs = ['TvShows', 'Movies', 'VariousUnsorted']
	for folderName, subfolders, filenames in os.walk(root):
		subfolders[:] = [d for d in subfolders if d not in excludedDirs]
		for filename in filenames:
			extension = filename.split(".")[-1]
			pathtofile = os.path.join(folderName, filename)
			if extension[0] is 'r':
				extension = 'rar'
			extpath = os.path.join(extension)
			if extension != 'DS_Store':
				if  os.path.exists(extpath):
					try:
						shutil.move(pathtofile, extpath)
					except:
						try:
							newpath = path
							newpath += str(counter)
							print(newpath)
							os.rename(path, newpath)
							shutil.move(newpath, dest)
						except:
							pass
				else:
					os.makedirs(extpath)
					try:
						shutil.move(pathtofile, extpath)
					except:
						pass
#found function.
# http://www.jacobtomlinson.co.uk/2014/02/16/python-script-recursively-remove-empty-folders-directories/
def removeEmptyFolders(path, removeRoot=True):
	'Function to remove empty folders'
	if not os.path.isdir(path):
		return

	# remove empty subfolders
	files = os.listdir(path)
	if len(files):
		for f in files:
			fullpath = os.path.join(path, f)
			if os.path.isdir(fullpath):
				removeEmptyFolders(fullpath)

	# if folder empty, delete it
	files = os.listdir(path)
	if len(files) == 0 and removeRoot:
		#print ("Removing empty folder:", path)
		os.rmdir(path)

 

def main():
	#ask for messy folder
	#source = '/Users/arniola/Documents/Python/python2015/Verkefni4/downloads_orginal copy/'
	source = input('Enter path to your disgusting folder folder (or drag it to here): ')
	os.chdir(source)

	print('Guessing if video files are movies tvshow or some other')
	checkFiles(source)
	
	print('Trying to sort other files into folders based on file ending ')
	sortLeftovers(source)
	
	print('Removing empty folders ')
	removeEmptyFolders(source)

if __name__ == "__main__":
	main()