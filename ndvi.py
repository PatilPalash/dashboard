# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:47:27 2022

@author: admin
"""

import rasterio, os
import numpy
from rasterio.plot import show
import matplotlib.pyplot as plt
import glob



dirpath = r"D:\NDVI\ndvi_input_img\Raw_Mosaic_Images"

search_criteria = "2*.tif"
q = os.path.join(dirpath, search_criteria)
print(q)

raster_fps = glob.glob(q)

raster_fps

for loop in raster_fps:
    with rasterio.open(loop) as src:
        band_red = src.read(3)
        print(band_red)
        print(loop)
        

        
for loop1 in raster_fps:
    with rasterio.open(loop1) as src:
        print(src)
        band_nir = src.read(4)
        print(band_nir)
        print(loop1)
       
#print(loop)
        
# Allow division by zero 
numpy.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI
ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)
print(ndvi)

# Set spatial characteristics of the output object to mirror the input
kwargs = src.meta
kwargs.update(
    dtype=rasterio.float32,
    count = 1)

#dstPath = r"D:\NDVI\ndvi_output"
# Create the file
#for i in range(1, dstPath.count + 1):
    
            
    #plt.imsave("ndvi_cmap.png", ndvi, cmap=plt.cm.summer)
    
    
#for outputfile in rasterio.open('output.tif', 'w' , **kwargs) as dst:
#    dst.write_band(1, ndvi.astype(rasterio.float32))


for i, line in enumerate(raster_fps, start=2):
    with rasterio.open("ndvi{0}.tif".format(i), 'w', **kwargs) as dst:
        dst.write_band(1, ndvi.astype(rasterio.float32))
        print(i, line)
        print(line)
        #dst.write(line)
    #fi=open("input_%s.data"%i,'w')
    #fi.write(line)
#fs.close()


        
    
    
