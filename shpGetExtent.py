from osgeo import ogr
import os

# Get a Layer's Extent
inShapefile = "A.SHP"
inDriver = ogr.GetDriverByName("ESRI Shapefile")
inDataSource = inDriver.Open(inShapefile, 0)
inLayer = inDataSource.GetLayer()
extent = inLayer.GetExtent()