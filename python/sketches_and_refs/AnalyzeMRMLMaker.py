import sys
import os
import shutil
from datetime import datetime
import xml.etree.ElementTree as ET
    



insertTagPrefix = '*************'
NUMBER_TAG = insertTagPrefix + "NUMBER"
IMG_FILENAME_TAG = insertTagPrefix + "IMG_FILENAME"
HDR_FILENAME_TAG = insertTagPrefix + "HDR_FILENAME"

changers = {
    'Volume': {
        'storageNodeRef': 'vtkMRMLVolumeArchetypeStorageNode' + NUMBER_TAG, 
        'id': 'vtkMRMLScalarVolumeNode' + NUMBER_TAG, 
        'displayNodeRef': 'vtkMRMLScalarVolumeDisplayNode' + NUMBER_TAG
    },
    'VolumeDisplay': {
        'id' : 'vtkMRMLScalarVolumeDisplayNode' + NUMBER_TAG
    },
    'VolumeArchetypeStorage': {
        'name': 'VolumeArchetypeStorage_' + NUMBER_TAG, 
        'id': 'vtkMRMLVolumeArchetypeStorageNode' + NUMBER_TAG,
        'fileListMember0': HDR_FILENAME_TAG, 
        'fileListMember1': IMG_FILENAME_TAG,
        'fileName': IMG_FILENAME_TAG
    }
}





adderTags = {
    
    'Volume':{
        'origin': '0 0 0',
        'hideFromEditors': 'false',
        'ijkToRASDirections': '-1   0   0 0   -1   0 0 0 1 ',
        'userTags': '',
        'selected': 'false',
        'spacing': '1.09375 1.09375 2',
        'name': 'W029_MR_20110614_preop_3_MD_WU_on_W029_MR_20110614_preop_20_TRA_T1_25mm.4dfp_1',
        'labelMap': '0',
        'storageNodeRef': 'vtkMRMLVolumeArchetypeStorageNode*************NUMBER',
        'attributes': 'LabelMap:0',
        'selectable': 'true',
        'id': 'vtkMRMLScalarVolumeNode*************NUMBER',
        'displayNodeRef': 'vtkMRMLScalarVolumeDisplayNode*************NUMBER',
    },
        
        
    'VolumeDisplay':{
        'clipping': 'false',
        'pointSize': '1',
        'color': '0.5 0.5 0.5',
        'upperThreshold': '32767',
        'sliceIntersectionVisibility': 'false',
        'scalarVisibility': 'false',
        'ambient': '0',
        'id': 'vtkMRMLScalarVolumeDisplayNode*************NUMBER',
        'frontfaceCulling': 'false',
        'edgeColor': '0 0 0',
        'selectedAmbient': '0.4',
        'selectedSpecular': '0.5',
        'hideFromEditors': 'true',
        'selected': 'false',
        'name': 'VolumeDisplay_21',
        'window': '2.90781',
        'sliceIntersectionThickness': '1',
        'autoThreshold': '0',
        'interpolation': '1',
        'opacity': '1',
        'power': '1',
        'visibility': 'true',
        'autoWindowLevel': '1',
        'applyThreshold': '0',
        'lighting': 'true',
        'interpolate': '1',
        'shading': 'true',
        'selectable': 'true',
        'diffuse': '1',
        'backfaceCulling': 'true',
        'scalarRange': '0 100',
        'tensorVisibility': 'false',
        'colorNodeID': 'vtkMRMLColorTableNodeGrey',
        'lowerThreshold': '-32768',
        'level': '1.05611',
        'vectorVisibility': 'false',
        'lineWidth': '1',
        'specular': '0',
        'selectedColor': '1 0 0',
        'interpolateTexture': 'false',
        'representation': '2',
        'edgeVisibility': 'false',
        'autoScalarRange': 'true',
    },
            
            
    'VolumeArchetypeStorage':{
        'UseOrientationFromFile': '1',
        'fileListMember1': '*************IMG_FILENAME',
        'fileListMember0': '*************HDR_FILENAME',
        'singleFile': '4',
        'hideFromEditors': 'true',
        'name': 'VolumeArchetypeStorage_*************NUMBER',
        'readState': '0',
        'selected': 'false',
        'fileName': '*************IMG_FILENAME',
        'centerImage': '0',
        'id': 'vtkMRMLVolumeArchetypeStorageNode*************NUMBER',
        'writeState': '4',
        'selectable': 'true',
        'useCompression': '1',
    }
}


        
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
               volumeTags = 'volumeTags = {'
               for child in rootElement:
                   
                   #print child.tag


                   
                   #---------------------------
                   # TODO: Scene view stuff -- may have to consider later
                   #---------------------------
                   #if child.tag == 'SceneView':
                       
                   #for c in child:
                   #print '\t', c.tag
                           #for attrib, value in child.attrib.iteritems():
                           #print '\t', attrib, value


                           
                   #print child.attrib

                   
                   if 'Volume' in child.tag:
                       volumeTags += "'%s':{\n"%(child.tag)
                       
                       for attrib, value in child.attrib.iteritems():
                           #volumeTags += '%s\t\t%s\t%s'%(child.tag, attrib, value)
                           
                           for tag, subTags in changers.iteritems():
                               if tag == child.tag:
                                   for subTagAttrib in subTags:
                                       #print subTagAttrib, attrib
                                       if subTagAttrib == attrib:
                                           value = subTags[subTagAttrib]
                           #else:
                           volumeTags += "\t'%s': '%s',\n"%(attrib, value)

                           #print volumeTags
                       volumeTags += '},\n\n\n' 
                    
               volumeTags += '}'
               print volumeTags

                           
if __name__ == "__main__":
    main()
