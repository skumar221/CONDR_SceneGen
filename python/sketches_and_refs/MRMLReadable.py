import sys
import os
import shutil
from datetime import datetime
import xml.etree.ElementTree as ET
    


    
def main():
    """
    """
    
    #------------------------------------
    # MAIN PARAMS
    #------------------------------------
    makeBackup = True
    rootDir = "../Scenes/W029_unmodified/"

   


    
    #------------------------------------
    #  os.Walk through the scripts directory
    #------------------------------------   
    mrmlFiles = {}

    sceneViewDict = {}

    newMrmlText = ''
    for root, dirs, files in os.walk(rootDir):
       for f in files:

           filename = (f).replace('\\', "/") 
           src = os.path.join(root, filename)

           #
           # Parse through the mrml files
           #
           if src.lower().endswith('cene.mrml'):
               import xml.dom.minidom

               xml = xml.dom.minidom.parse(src) # or xml.dom.minidom.parseString(xml_string)
               pretty_xml_as_string = xml.toprettyxml()
               prettyStr = pretty_xml_as_string.replace('" ', '"\n') 
               prettyStr = prettyStr.split('\n')

               currSpacer = ''
               newLines = []
               for line in prettyStr:
                   newLine = line
                   if '<' in line:
                       currSpacer = line.split('<')[0]
                       newLines.append('\n' + newLine)
                   elif '=' in line:
                       newLine = currSpacer + '\t' + newLine.strip()
                       newLines.append(newLine)


               newLines2 = []
               for line in newLines:
                   if '<' in line and '=' in line:
                       currSpacer = line.split('<')[0].replace('\n', '') 
                       partLine = line.partition(' ')
                       newLines2.append(partLine[0])
                       newLines2.append(currSpacer + '\t' + partLine[2])
                   else:
                       newLines2.append(line)

               theFile = open(rootDir + 'humanReadable.mrml', 'w')
               for item in newLines2:
                   print>>theFile, item
               theFile.close()
                
if __name__ == "__main__":
    main()
