#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import gdal

# Set the input images
input_images = ['/path/to/image1.tif', '/path/to/image2.tif', '/path/to/image3.tif']

# Set the output mosaic image
output_image = '/path/to/mosaic.tif'

# Open the first image to get the information
first_image = gdal.Open(input_images[0])

# Set the output driver
output_driver = gdal.GetDriverByName('GTiff')

# Create the output mosaic image
output = output_driver.Create(output_image, first_image.RasterXSize, first_image.RasterYSize, len(input_images), first_image.GetRasterBand(1).DataType)

# Set the projection and geotransform of the output mosaic image
output.SetProjection(first_image.GetProjection())
output.SetGeoTransform(first_image.GetGeoTransform())

# Loop through the input images and copy them into the output mosaic image
for i, image in enumerate(input_images):
    input = gdal.Open(image)
    for j in range(1, input.RasterCount + 1):
        output.GetRasterBand(j + i).WriteArray(input.GetRasterBand(j).ReadAsArray())

# Close all the images
for image in [first_image, input, output]:
    image = None

