import zipfile
import os
#imports zipfiles

path = r"C:\Users\benwa\Desktop\test"
#sets the path that the rest of the program will be working on

os.chdir(path) #changes directory to path that was previously set


offset = 0 #initiates the while loop variable

while offset != 50 : #starts the while loop to iterate through all zipped files. This should be however many files you're iterating through
    if offset > 9 : #I needed an if statement to fix exceptions because my file names start with a 0 if before 10 (01, 02, 3... 10, 11, 12 etc)
        filename = "lesson-" + str(offset) + ".zip" #filename is a string that takes the first half of the file name (yours will be different), concatenates that file name with its number in the sequence, which increments by 1 each while loop
    else:  
        filename = "lesson-0" + str(offset) + ".zip" 
    with zipfile.ZipFile(filename) as f: # unzips the file "filename" if found in the declared path variable 
        f.extractall() # extracts everything in zipped file
        offset += 1 
