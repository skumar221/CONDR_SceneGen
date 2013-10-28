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
    for root, dirs, files in os.walk(rootDir):
       for f in files:

           filename = (f).replace('\\', "/") 
           src = os.path.join(root, filename)

           #
           # Parse through the mrml files
           #
           if src.lower().endswith('.mrml'):
               mrmlFiles[src] = ET.parse(src)
               rootElement = mrmlFiles[src].getroot()
               #print rootElement.tag, rootElement.attrib
               for child in rootElement:
                   
                   #print child.tag


                   
                   #---------------------------
                   # TODO: Scene view stuff -- may have to consider later
                   #---------------------------
                   if child.tag == 'SceneView':
                       print child.tag
                       for c in child:
                           #print '\t', c.tag
                           print c.tag
                           for attrib in c:
                               print '\t\t', attrib


                           
                   #print child.attrib
                   #hasFile = False
                   #if 'Volume' in child.tag:

                    
               return

                           
if __name__ == "__main__":
    main()
