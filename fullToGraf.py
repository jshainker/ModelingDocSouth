# code to split an entire text (memoir, biography, etc.) into its component paragraphs

import re
import os

# change working directory (and check to make sure it worked)
malletDir = 'c:\\mallet\\hist-data\\texts'
os.chdir(malletDir)
print("Current working directory:", malletDir)

# create a new folder for the split texts
savepath = malletDir + '\\textsgrafs'
os.mkdir(savepath)

# cycle through each text in the folder
for text in os.listdir(malletDir):

# open text file, read it into a variable, 
# remove bracketed info, and write each paragraph into its own file
    with open(text,  'r', encoding="utf8") as file:
        
        # read file name into variable and check
        title = text
        print (title)
        
        #read file into variable, close the file, and continue
        var = file.read()
        file.close()
        pass

        # remove bracketed text (useless image information)
        modified_var = re.sub(r"\[(.*?)\]", "", var)

        # split text into paragraphs
        splat=modified_var.split("\n")

        # for each individual paragraph, name it and write it into its own file 
        for number, paragraph in enumerate (splat, 1):
            
            # ignore null paragraphs
            if paragraph == "":
                continue

            # save new filename
            filename = title + '_graf' + str(number) + '.txt.'

            # change to directory where I want to save my grafs
            os.chdir(savepath)
            
            #open new files and write paragraphs into them one at a time
            with open(filename, 'w', encoding="utf8") as file:
                file.write(paragraph)
                file.close()
                pass
            
            #change back to directory with full texts
            os.chdir(malletDir)
