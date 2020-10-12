import os
import sys
import re

vtk_version = '8.2'
vtklibreleases = ['vtkalglib-' + vtk_version, 'vtkChartsCore-' + vtk_version, 'vtkCommonColor-' + vtk_version, 'vtkCommonComputationalGeometry-' + vtk_version, 'vtkCommonCore-' + vtk_version, 'vtkCommonDataModel-' + vtk_version, 'vtkCommonExecutionModel-' + vtk_version, 'vtkCommonMath-' + vtk_version, 'vtkCommonMisc-' + vtk_version, 'vtkCommonSystem-' + vtk_version, 'vtkCommonTransforms-' + vtk_version, 'vtkDICOMParser-' + vtk_version, 'vtkDomainsChemistry-' + vtk_version, 'vtkDomainsChemistry-' + vtk_version, 'vtkexoIIc-' + vtk_version, 'vtkFiltersAMR-' + vtk_version, 'vtkFiltersCore-' + vtk_version, 'vtkFiltersExtraction-' + vtk_version, 'vtkFiltersFlowPaths-' + vtk_version, 'vtkFiltersGeneral-' + vtk_version, 'vtkFiltersGeneric-' + vtk_version, 'vtkFiltersGeometry-' + vtk_version, 'vtkFiltersHybrid-' + vtk_version, 'vtkFiltersHyperTree-' + vtk_version, 'vtkFiltersImaging-' + vtk_version, 'vtkFiltersModeling-' + vtk_version, 'vtkFiltersParallel-' + vtk_version, 'vtkFiltersParallelImaging-' + vtk_version, 'vtkFiltersPoints-' + vtk_version, 'vtkFiltersProgrammable-' + vtk_version, 'vtkFiltersSelection-' + vtk_version, 'vtkFiltersSMP-' + vtk_version, 'vtkFiltersSources-' + vtk_version, 'vtkFiltersStatistics-' + vtk_version, 'vtkFiltersTexture-' + vtk_version, 'vtkFiltersTopology-' + vtk_version, 'vtkFiltersVerdict-' + vtk_version, 'vtkGeovisCore-' + vtk_version, 'vtkgl2ps-' + vtk_version, 'vtkImagingColor-' + vtk_version, 'vtkImagingCore-' + vtk_version, 'vtkImagingFourier-' + vtk_version, 'vtkImagingGeneral-' + vtk_version, 'vtkImagingHybrid-' + vtk_version, 'vtkImagingMath-' + vtk_version, 'vtkImagingMorphological-' + vtk_version, 'vtkImagingSources-' + vtk_version, 'vtkImagingStatistics-' + vtk_version, 'vtkImagingStencil-' + vtk_version, 'vtkInfovisCore-' + vtk_version, 'vtkInfovisLayout-' + vtk_version, 'vtkInteractionImage-' + vtk_version, 'vtkInteractionStyle-' + vtk_version, 'vtkInteractionWidgets-' + vtk_version, 'vtkIOAMR-' + vtk_version, 'vtkIOCore-' + vtk_version, 'vtkIOEnSight-' + vtk_version, 'vtkIOExodus-' + vtk_version, 'vtkIOExport-' + vtk_version, 'vtkIOExport-' + vtk_version, 'vtkIOGeometry-' + vtk_version, 'vtkIOImage-' + vtk_version, 'vtkIOImport-' + vtk_version, 'vtkIOInfovis-' + vtk_version, 'vtkIOLegacy-' + vtk_version, 'vtkIOLSDyna-' + vtk_version, 'vtkIOMINC-' + vtk_version, 'vtkIOMovie-' + vtk_version, 'vtkIONetCDF-' + vtk_version, 'vtkIOParallel-' + vtk_version, 'vtkIOParallelXML-' + vtk_version, 'vtkIOPLY-' + vtk_version, 'vtkIOSQL-' + vtk_version, 'vtkIOTecplotTable-' + vtk_version, 'vtkIOVideo-' + vtk_version, 'vtkIOXML-' + vtk_version, 'vtkIOXMLParser-' + vtk_version, 'vtklibharu-' + vtk_version, 'vtkmetaio-' + vtk_version, 'vtknetcdfcpp-' + vtk_version, 'vtkoggtheora-' + vtk_version, 'vtkParallelCore-' + vtk_version, 'vtkproj4-' + vtk_version, 'vtkRenderingAnnotation-' + vtk_version, 'vtkRenderingContext2D-' + vtk_version, 'vtkRenderingContextOpenGL-' + vtk_version, 'vtkRenderingCore-' + vtk_version, 'vtkRenderingFreeType-' + vtk_version, 'vtkRenderingGL2PS-' + vtk_version, 'vtkRenderingImage-' + vtk_version, 'vtkRenderingLabel-' + vtk_version, 'vtkRenderingLOD-' + vtk_version, 'vtkRenderingOpenGL-' + vtk_version, 'vtkRenderingVolume-' + vtk_version, 'vtkRenderingVolumeOpenGL-' + vtk_version, 'vtksqlite-' + vtk_version, 'vtksys-' + vtk_version, 'vtkverdict-' + vtk_version, 'vtkViewsContext2D-' + vtk_version, 'vtkViewsCore-' + vtk_version, 'vtkViewsInfovis-' + vtk_version,  'vtkzlib-' + vtk_version]

#print(len(vtklibreleases))
os.chdir(r'C:\Program Files\PCL 1.11.0\3rdParty\VTK\lib')
print(os.getcwd())
lib_list = os.listdir()
print(lib_list)
liblist = []
for i in lib_list:

    #print(i)
    lib_match = re.match('.*8.2.lib$',i)
    if lib_match != None:
        print(lib_match.group())
        lib_match = lib_match.group()
        liblist.append(lib_match)
        
print(liblist)
print(len(liblist))
