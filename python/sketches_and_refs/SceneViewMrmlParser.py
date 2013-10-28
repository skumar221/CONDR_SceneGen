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
                   
                   
                   if child.tag == 'SceneView':
                       print '<SceneView '
                       for atr, val in child.attrib.iteritems():
                           print '\t%s= "%s" '%(atr, val)
                       print '>'

                       for c in child:

                           #
                           # Let's see if the 'Volume' based nodes are the same...
                           #
                           if 'Volume' in c.tag:
                               continue
                           
                           print '\t<%s'%(c.tag)
                           for attrib, value in c.attrib.iteritems():
                               print '\t\t%s= "%s"'%(attrib, value)
                           print '\t></%s>'%(c.tag)
                       print '</SceneView>'
                           
if __name__ == "__main__":
    main()
