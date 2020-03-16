import os
import argparse
import shutil

#where to search
toSearch = "/Users/guillaume.hyvert/Desktop/CPMA1"
#file where the results are going to be copied
toMoveto = "/Users/guillaume.hyvert/Desktop/tomoveto"
#dictory who will be ignored
exception = "/Users/guillaume.hyvert/Desktop/CPMA1/test"
#location of the temporary file
temp = "/tmp"
#extension to search for (can be only a part of it)(example: .fmp for .fmp12 files)
extension = ".fmp"
new_file_name = ""

os.mkdir(os.path.join(temp+'/temp'))

#searching recursively
for root, dirs, files in os.walk(toSearch):
    #for each file
    for every in files:
        #ignore the file if he is in the exception directory
        if str(os.path.join(root, every)).find(exception):
            #if the extension contains ".fmp"
            if str(every).find(".fmp"):
                new_file_name = every
                #check if a file with the same name exist in the temp file
                if os.path.isfile(os.path.join(temp+'/temp/'+new_file_name)):
                    expand = 1
                    while True:
                        #add a number before the extension who will increase if it already exists
                        expand += 1
                        new_file_name = every.split(".fmp12")[0] + "-" + str(expand) + ".fmp12"
                        if os.path.isfile(os.path.join(temp+'/temp/'+new_file_name)):
                            continue
                        else:
                            break
                #moving the file into the temp file (and changing the name of it)
                shutil.move(os.path.join(root, every),os.path.join(temp+'/temp/'+new_file_name))
#moving the temp file to the destination
shutil.move(os.path.join(temp+'/temp'), toMoveto)