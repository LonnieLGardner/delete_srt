import sys
import os
import glob


# THIS IS A SIMPLE SCRIPT TO DELETE ALL .srt FILES IN A DIRECTOR.
# ALSO YOU CAN ALWAYS CHANGE THE EXTENSION '.srt' TO '.vtt' OR WHAT EVER YOU NEED


current_dir = os.getcwd()

for(dirname, dirs, files) in os.walk(current_dir):
	for file in files:
		if file.endswith('.srt'):
			source_file = os.path.join(dirname, file)
			os.remove(source_file)
