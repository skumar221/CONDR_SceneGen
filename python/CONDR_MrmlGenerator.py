import sys
import os
import shutil
from datetime import datetime
import xml.etree.ElementTree as ET
    



insertTagPrefix = '*************'
NUMBER_TAG = insertTagPrefix + "NUMBER"
IMG_FILENAME_TAG = insertTagPrefix + "IMG_FILENAME"
HDR_FILENAME_TAG = insertTagPrefix + "HDR_FILENAME"
VOLUME_NAME_TAG = insertTagPrefix + "VOLUME_NAME_TAG"


SELECTED_VTK_MRML_SCALAR_VOLUME_NODE = "SELECTED_VTK_MRML_SCALAR_VOLUME_NODE"


changers = {
    'Volume': {
        'name': VOLUME_NAME_TAG,
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
        'name': VOLUME_NAME_TAG,
        'labelMap': '0',
        'storageNodeRef': 'vtkMRMLVolumeArchetypeStorageNode' + NUMBER_TAG,
        'attributes': 'LabelMap:0',
        'selectable': 'true',
        'id': 'vtkMRMLScalarVolumeNode' + NUMBER_TAG,
        'displayNodeRef': 'vtkMRMLScalarVolumeDisplayNode' + NUMBER_TAG,
    },
        
        
    'VolumeDisplay':{
        'clipping': 'false',
        'pointSize': '1',
        'color': '0.5 0.5 0.5',
        'upperThreshold': '32767',
        'sliceIntersectionVisibility': 'false',
        'scalarVisibility': 'false',
        'ambient': '0',
        'id': 'vtkMRMLScalarVolumeDisplayNode' + NUMBER_TAG,
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
        'fileListMember1': IMG_FILENAME_TAG,
        'fileListMember0': HDR_FILENAME_TAG,
        'singleFile': '4',
        'hideFromEditors': 'true',
        'name': 'VolumeArchetypeStorage_' + NUMBER_TAG,
        'readState': '0',
        'selected': 'false',
        'fileName': IMG_FILENAME_TAG,
        'centerImage': '0',
        'id': 'vtkMRMLVolumeArchetypeStorageNode' + NUMBER_TAG,
        'writeState': '4',
        'selectable': 'true',
        'useCompression': '1',
    }
}



sceneViewStr = """
<SceneView 
	selected= "false" 
	hideFromEditors= "false" 
	userTags= "" 
	sceneViewDescription= "Scene at MRML file save point" 
	id= "vtkMRMLSceneViewNode1" 
	storageNodeRef= "vtkMRMLSceneViewStorageNode1" 
	selectable= "true" 
	screenshotType= "4" 
	name= "Master Scene View" 
>
	<Crosshair
		crosshairMode= "NoCrosshair"
		hideFromEditors= "true"
		crosshairRAS= "0 0 0"
		selected= "false"
		crosshairThickness= "Fine"
		crosshairBehavior= "Normal"
		selectable= "true"
		navigation= "false"
		id= "vtkMRMLCrosshairNodedefault"
		name= "Crosshair"
	></Crosshair>
    
	<Selection
		activeFiducialListID= "NULL"
		activeViewID= "NULL"
		timeUnitNodeRef= "vtkMRMLUnitNodeApplicationTime"
		activeLayoutID= "NULL"
		activePlaceNodeClassName= "NULL"
		activePlaceNodeID= "NULL"
		activeCameraID= "NULL"
		selectable= "true"
		name= "Selection"
		secondaryVolumeID= "vtkMRMLScalarVolumeNode*************NUMBER"
		hideFromEditors= "true"
		selected= "false"
		id= "vtkMRMLSelectionNodeSingleton"
		activeROIListID= "NULL"
		activeVolumeID= "vtkMRMLScalarVolumeNode*************NUMBER"
		activeLabelVolumeID= "NULL"
		lengthUnitNodeRef= "vtkMRMLUnitNodeApplicationLength"
	></Selection>
    
	<Interaction
		hideFromEditors= "true"
		name= "Interaction"
		selectable= "true"
		lastInteractionMode= "ViewTransform"
		selected= "false"
		currentInteractionMode= "ViewTransform"
		id= "vtkMRMLInteractionNodeSingleton"
	></Interaction>
    
	<View
		rockLength= "200"
		letterSize= "0.05"
		backgroundColor2= "0.454902 0.470588 0.745098"
		animationMode= "Off"
		fieldOfView= "200"
		useDepthPeeling= "0"
		visibility= "false"
		axisLabelsVisible= "true"
		attributes= "MappedInLayout:1"
		active= "false"
		selectable= "true"
		renderMode= "Perspective"
		id= "vtkMRMLViewNode1"
		spinDirection= "YawLeft"
		name= "View1"
		axisLabelsCameraDependent= "true"
		hideFromEditors= "false"
		stereoType= "NoStereo"
		boxVisible= "true"
		selected= "false"
		rotateDegrees= "5"
		layoutName= "1"
		spinDegrees= "2"
		layoutLabel= "1"
		backgroundColor= "0.756863 0.764706 0.909804"
		fiducialLabelsVisible= "true"
		viewAxisMode= "LookFrom"
		rockCount= "0"
		spinMs= "5"
		fiducialsVisible= "true"
	></View>
    
	<Slice
		sliceVisibility= "false"
		orientation= "Axial"
		sliceSpacingMode= "0"
		xyzOrigin= "0 0 0"
		orientationReference= "Axial"
		uvwExtents= "280 316.554 2"
		id= "vtkMRMLSliceNodeRed"
		hideFromEditors= "false"
		uvwDimensions= "256 256 1"
		layoutGridRows= "1"
		selected= "false"
		layoutName= "Red"
		sliceToRAS= "-1 0 0 -139.453 0 1 0 -139.453 0 0 1 96 0 0 0 1"
		backgroundColor= "0 0 0"
		sliceResolutionMode= "1"
		activeSlice= "0"
		prescribedSliceSpacing= "1 1 1"
		uvwOrigin= "0 0 0"
		layoutGridColumns= "1"
		selectable= "true"
		backgroundColor2= "0 0 0"
		fieldOfView= "280 316.554 2"
		visibility= "false"
		active= "false"
		useLabelOutline= "false"
		jumpMode= "1"
		dimensions= "383 433 1"
		widgetVisibility= "false"
		name= "Red"
		layoutLabel= "R"
		layoutColor= "0.952941 0.290196 0.2"
		attributes= "MappedInLayout:1"
	></Slice>
    
	<Slice
		sliceVisibility= "false"
		orientation= "Sagittal"
		sliceSpacingMode= "0"
		xyzOrigin= "0 0 0"
		orientationReference= "Sagittal"
		uvwExtents= "280 316.554 1.09375"
		id= "vtkMRMLSliceNodeYellow"
		hideFromEditors= "false"
		uvwDimensions= "256 256 1"
		layoutGridRows= "1"
		selected= "false"
		layoutName= "Yellow"
		sliceToRAS= "0 0 1 -138.906 -1 0 0 -139.453 0 1 0 95 0 0 0 1"
		backgroundColor= "0 0 0"
		sliceResolutionMode= "1"
		activeSlice= "0"
		prescribedSliceSpacing= "1 1 1"
		uvwOrigin= "0 0 0"
		layoutGridColumns= "1"
		selectable= "true"
		backgroundColor2= "0 0 0"
		fieldOfView= "280 316.554 1.09375"
		visibility= "false"
		active= "false"
		useLabelOutline= "false"
		jumpMode= "1"
		dimensions= "383 433 1"
		widgetVisibility= "false"
		name= "Yellow"
		layoutLabel= "Y"
		layoutColor= "0.929412 0.835294 0.298039"
		attributes= "MappedInLayout:1"
	></Slice>
    
	<Slice
		sliceVisibility= "false"
		orientation= "Coronal"
		sliceSpacingMode= "0"
		xyzOrigin= "0 0 0"
		orientationReference= "Coronal"
		uvwExtents= "280 317.382 1.09375"
		id= "vtkMRMLSliceNodeGreen"
		hideFromEditors= "false"
		uvwDimensions= "256 256 1"
		layoutGridRows= "1"
		selected= "false"
		layoutName= "Green"
		sliceToRAS= "-1 0 0 -139.453 0 0 1 -138.906 0 1 0 95 0 0 0 1"
		backgroundColor= "0 0 0"
		sliceResolutionMode= "1"
		activeSlice= "0"
		prescribedSliceSpacing= "1 1 1"
		uvwOrigin= "0 0 0"
		layoutGridColumns= "1"
		selectable= "true"
		backgroundColor2= "0 0 0"
		fieldOfView= "280 317.382 1.09375"
		visibility= "false"
		active= "false"
		useLabelOutline= "false"
		jumpMode= "1"
		dimensions= "382 433 1"
		widgetVisibility= "false"
		name= "Green"
		layoutLabel= "G"
		layoutColor= "0.431373 0.690196 0.294118"
		attributes= "MappedInLayout:1"
	></Slice>
    
	<Layout
		collapseSliceControllers= "0"
		name= "Layout"
		bottomPanelVisibility= "1"
		mainPanelSize= "400"
		numberOfCompareViewColumns= "1"
		selectable= "true"
		id= "vtkMRMLLayoutNodevtkMRMLLayoutNode"
		numberOfLightboxColumns= "6"
		hideFromEditors= "true"
		numberOfLightboxRows= "6"
		secondaryPanelSize= "400"
		selected= "false"
		numberOfCompareViewRows= "1"
		guiPanelVisibility= "1"
		guiPanelLR= "0"
		currentViewArrangement= "0"
	></Layout>
    
	<Camera
		hideFromEditors= "false"
		name= "Default Scene Camera"
		id= "vtkMRMLCameraNode1"
		selected= "false"
		activetag= "vtkMRMLViewNode1"
		position= "0 500 0"
		parallelScale= "1"
		appliedTransform= "1 0 0 0  0 1 0 0  0 0 1 0  0 0 0 1"
		viewUp= "0 0 1"
		parallelProjection= "false"
		selectable= "true"
		focalPoint= "0 0 0"
	></Camera>
    
	<SliceComposite
		foregroundVolumeID= ""
		labelOpacity= "1"
		sliceIntersectionVisibility= "0"
		backgroundVolumeID= "vtkMRMLScalarVolumeNode*************NUMBER"
		name= "SliceComposite"
		labelGrid= "1"
		labelVolumeID= ""
		doPropagateVolumeSelection= "1"
		foregroundGrid= "0"
		fiducialVisibility= "1"
		fiducialLabelVisibility= "1"
		selectable= "true"
		id= "vtkMRMLSliceCompositeNodeRed"
		foregroundOpacity= "0"
		hideFromEditors= "true"
		annotationMode= "All"
		selected= "false"
		layoutName= "Red"
		backgroundGrid= "0"
		linkedControl= "0"
		compositing= "0"
		annotationSpace= "IJKAndRAS"
	></SliceComposite>
    
	<SliceComposite
		foregroundVolumeID= ""
		labelOpacity= "1"
		sliceIntersectionVisibility= "0"
		backgroundVolumeID= "vtkMRMLScalarVolumeNode*************NUMBER"
		name= "SliceComposite_1"
		labelGrid= "1"
		labelVolumeID= ""
		doPropagateVolumeSelection= "1"
		foregroundGrid= "0"
		fiducialVisibility= "1"
		fiducialLabelVisibility= "1"
		selectable= "true"
		id= "vtkMRMLSliceCompositeNodeYellow"
		foregroundOpacity= "0"
		hideFromEditors= "true"
		annotationMode= "All"
		selected= "false"
		layoutName= "Yellow"
		backgroundGrid= "0"
		linkedControl= "0"
		compositing= "0"
		annotationSpace= "IJKAndRAS"
	></SliceComposite>
    
	<SliceComposite
		foregroundVolumeID= ""
		labelOpacity= "1"
		sliceIntersectionVisibility= "0"
		backgroundVolumeID= "vtkMRMLScalarVolumeNode*************NUMBER"
		name= "SliceComposite_2"
		labelGrid= "1"
		labelVolumeID= ""
		doPropagateVolumeSelection= "1"
		foregroundGrid= "0"
		fiducialVisibility= "1"
		fiducialLabelVisibility= "1"
		selectable= "true"
		id= "vtkMRMLSliceCompositeNodeGreen"
		foregroundOpacity= "0"
		hideFromEditors= "true"
		annotationMode= "All"
		selected= "false"
		layoutName= "Green"
		backgroundGrid= "0"
		linkedControl= "0"
		compositing= "0"
		annotationSpace= "IJKAndRAS"
	></SliceComposite>
    
	<ClipModels
		hideFromEditors= "true"
		selectable= "true"
		selected= "false"
		name= "ClipModels"
		redSliceClipState= "0"
		greenSliceClipState= "0"
		clipType= "0"
		id= "vtkMRMLClipModelsNodevtkMRMLClipModelsNode"
		yellowSliceClipState= "0"
	></ClipModels>
</SceneView>"""



        
def main():
    """
    """
    
    #------------------------------------
    # MAIN PARAMS
    #------------------------------------
    makeBackup = True
    fileDir = "../sample-data/W029_unmodified/"
    refTextDir = "../xml"
    sceneDir = os.path.dirname(os.path.dirname(fileDir))
   


    
    #------------------------------------
    #  Gather the analyze pairngs
    #------------------------------------   
    filePairs = []
    for root, dirs, files in os.walk(fileDir):
       for f in files:
           # '\n'
           #print f
           if f.lower().endswith('.img'):
               filePath = './' + os.path.basename(os.path.dirname(root))
               imgFileName = f
               #print "IMG:\t" + imgFileName

               imgFileName = imgFileName.replace('.IMG', '.img')
               hdrFileName = imgFileName.replace('.img', '.hdr') 
               if os.path.exists(os.path.join(root, hdrFileName)):
                   filePairs.append({'img': os.path.join(filePath, imgFileName),'hdr':os.path.join(filePath, hdrFileName)})



    volumesString = ''
    nodeCounter = 1
    adderTagOrder = ['Volume', 'VolumeDisplay', 'VolumeArchetypeStorage']
    for filePair in filePairs:
        for adderTag in adderTagOrder:
            volumesString += '<%s\n'%(adderTag)


            for subAdderTag, value in adderTags[adderTag].iteritems():
                if insertTagPrefix in value:
                    #print changers[adderTag][subAdderTag]


                    #
                    # Number Tags
                    #
                    if NUMBER_TAG in value:
                        value = value.replace(NUMBER_TAG, str(nodeCounter))


                    elif IMG_FILENAME_TAG in value:
                        value = value.replace(IMG_FILENAME_TAG, str(filePair['img']))

                        
                    elif HDR_FILENAME_TAG in value: 
                        value = value.replace(HDR_FILENAME_TAG, str(filePair['hdr']))

                        
                    elif VOLUME_NAME_TAG in value: 
                        value = value.replace(VOLUME_NAME_TAG, os.path.basename(filePair['img'].replace('.img','')))

                    volumesString += '\t%s= "%s"\n'%(subAdderTag, value)

                else:
                    volumesString += '\t%s= "%s"\n'%(subAdderTag, value)


                
            volumesString += '></%s>\n\n'%(adderTag)

            
        nodeCounter += 1




    #-----------------------
    # Add the prefix xml
    #-----------------------      
    autoGeneratedMrmlText = ''
    with open(os.path.join(refTextDir, 'beginning.xml')) as f:
        beginningContents = f.readlines()
        
    for beginningContent in beginningContents:
        autoGeneratedMrmlText += beginningContent

    autoGeneratedMrmlText += '\n' + volumesString + '\n'

    

    #-----------------------
    # Add the scene view xml
    #-----------------------
    with open(os.path.join(refTextDir, 'sceneview.xml')) as f:
        sceneViewContents = f.readlines()

        
    for sceneViewContent in sceneViewContents:
        autoGeneratedMrmlText += sceneViewContent.replace('\t\t','\t')

    volumesString = volumesString.replace('\n', '\n\t')
    autoGeneratedMrmlText = autoGeneratedMrmlText.replace('INSERT_VOLUMES_HERE', volumesString) 

    #autoGeneratedMrmlText += '\n</SceneView>\n\n'



    #-----------------------
    # Add the suffix xml
    #-----------------------
    autoGeneratedMrmlText += '\n'
    with open(os.path.join(refTextDir, 'end.xml')) as f:
        endContents = f.readlines()
        
    for endContent in endContents:
        autoGeneratedMrmlText += endContent
    


    #-----------------------
    # Replace the selected 'SELECTED_VTK_MRML_SCALAR_VOLUME_NODE' tag with 
    # 'vtkMRMLScalarVolumeNode'
    #-----------------------
    selectedVolumeNumber = str(nodeCounter - 1) 
    autoGeneratedMrmlText = autoGeneratedMrmlText.replace(SELECTED_VTK_MRML_SCALAR_VOLUME_NODE, 'vtkMRMLScalarVolumeNode' + selectedVolumeNumber)


    

    autoGeneratedMrmlText = "<!-- THIS IS AN AUTO-GENERATED MRML -->\n" + autoGeneratedMrmlText


    
    newMrmlFileName = os.path.join(sceneDir, "AUTO-GENERATED_%s_Scene.mrml"%(os.path.basename(sceneDir)))
    newMrmlFile = open(newMrmlFileName, "w")
    newMrmlFile.write(autoGeneratedMrmlText)
    newMrmlFile.close()

 

if __name__ == "__main__":
    main()
