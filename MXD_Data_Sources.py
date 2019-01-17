# -------------------------------------------------------------------------------
# Name:       MXD_Data_Sources.py
# Purpose:    Find all Map Documents within a folder or sub folder.
#             Report map directory, layers in each map document, source path of each layer and
#             definition queries on layers (if any).
#             Writes this information to a user-specified csv file.
#
# Author:      Alexander Brown - Geospatial Systems Analyst
#              Alexander.Brown@phila.gov
# Date: 02/08/2015
#
# Revised: 07/18/2018 by Alexander Brown - Solution Engineer ESRI alexander_brown@esri.com
# -------------------------------------------------------------------------------

# Import system modules
import os
import arcpy
import csv
import arcpy
from arcpy import env

# Change 'root_folder' to directory with MXDs
root_folder = r"D:\\"

# Location & name of output CSV file to write to
csv_file = r"D:\MXD_output_test.csv"

# Specify sub-folders to ignore (optional), blank example below
# ignore_folders = [r'F:\MXD\PhilaGov\Archive', r'F:\MXD\PhilaGov\Data', r'F:\MXD\PhilaGov\TEST\NO']
ignore_folders = []


# Function to loop through each mxd
def report_layers(mxd_list):
    mxd = mxd_list[i]
    mxd_name = mxd.rsplit("\\", 1)[1]
    work_space = mxd.rsplit("\\", 1)[0]
    try:
        map_doc = arcpy.mapping.MapDocument(mxd)
    except RuntimeError as e:
        print(e)
        def_query = 'Please check your MXD, open it manually is it corrupt? Run MXD Doctor.'
        layer = 'None'
        source = 'None'
        writer.writerow({'Directory': work_space, 'MapDoc': mxd_name, 'Layer': layer, 'Source': source,
                         'Definition_Query': def_query})
        map_doc = ''
        pass
    except TypeError as e:
        print(e)
        def_query = 'Please check your MXD, open it manually is it corrupt? Run MXD Doctor.'
        layer = 'None'
        source = 'None'
        writer.writerow({'Directory': work_space, 'MapDoc': mxd_name, 'Layer': layer, 'Source': source,
                         'Definition_Query': def_query})
        map_doc = ''
        pass

    if map_doc == '':
        pass
    else:

        # List all layers in mxd
        new_list = arcpy.mapping.ListLayers(map_doc)
        # Grab layer attributes and write to csv row
        for lyr in new_list:
            if lyr.supports("dataSource"):
                print("Layer: " + lyr.name + " | " + "  Source: " + lyr.dataSource)
                layer = str(lyr.name)
                source = str(lyr.dataSource)
                if lyr.supports("definitionQuery"):
                    def_query = str(lyr.definitionQuery)
                else:
                    def_query = ' '

                writer.writerow({'Directory': work_space, 'MapDoc': mxd_name, 'Layer': layer, 'Source': source,
                                 'Definition_Query': def_query})
            elif lyr.isGroupLayer:
                pass
            else:
                layer = str(lyr.name)
                source = 'Could not report source'
                def_query = 'Please check your MXD, open it manually is it corrupt? Run MXD Doctor.'
                writer.writerow({'Directory': work_space, 'MapDoc': mxd_name, 'Layer': layer, 'Source': source,
                                 'Definition_Query': def_query})


if __name__ == "__main__":

    mxdList = []

    # Loop through all operating system directories to build list in memory of mxds
    for root, dirs, files in os.walk(root_folder):
        if root in ignore_folders:
            pass
        else:
            for mxd_file in files:
                if mxd_file.endswith(".mxd"):
                    mxdList.append(os.path.join(root, mxd_file))

    # Open csv file and establish the dictionary writer
    with open(csv_file, 'w') as csv_file:
        # Set header field names
        fieldname = ['Directory', 'MapDoc', 'Layer', 'Source', 'Definition_Query']

        writer = csv.DictWriter(csv_file, fieldnames=fieldname, delimiter='\n')

        # Loop through workspace list
        for i in range(len(mxdList)):

            # If first iteration write header line to csv file
            if i == 0:
                writer.writeheader()
                print("Header line written...")
                print("*****" + str(mxdList[i]))
                report_layers(mxdList)

            else:
                report_layers(mxdList)
                print("*****" + str(mxdList[i]))

    print("***** Script Finished *****")
