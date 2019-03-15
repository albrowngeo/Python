# Python Workflows with ArcGIS

Supporting scripts for Harrsiburg GeoDev

Abstract:
Facilitating the movement of data is crucial for organizations across the country. Whether in the government or private sectors, the skills to Extract Transform & Load (ETL) data are critical for maintaining production system workflows & viability. Esri provides two python frameworks for interfacing across a modern Web GIS. Arcpy is a Python site package that provides powerful geographic data analysis, conversion, management and automation. ArcGIS Python API is a powerful, modern, and easy to use Pythonic API for GIS professionals, developers, administrators, content publishers or anyone trying to accomplish ETL workflows within ArcGIS. The session will begin with introducing the Python API for Feature Service querying and data movement. However, the primary focus will be combining the ArcPy and Python API libraries for various ETL processes.

## Getting Started

Download the scripts and import into Jupyter notebooks or desktop IDE of choice.  Make sure you have the relavant libraries.

### Prerequisites

* Python API
* ArcPy
* ArcGIS Enterprise or ArcGIS Online
    * Named user account license in the organization
    * ArcGIS Pro License assigned to named user account

### Installing

* [Install the ArcGIS Python API](https://developers.arcgis.com/python/guide/install-and-set-up/)
* [Install ArcGIS Pro](https://pro.arcgis.com/en/pro-app/get-started/install-and-sign-in-to-arcgis-pro.htm)


## Deployment

Add additional notes about how to deploy this on a live system

## Data

* [Philly Crime](https://www.opendataphilly.org/dataset/crime-incidents) - Philadelphia Open Data

For Demonstration Purposes, created subsets of the data for testing.

   * **Overwrite Content with CSV  |  55 Records**
        * Adds features by uploading csv
        
 
   * **Add Features from SDE - v1  |  55 Records**
        * Adds features one by one using
        * Utilizes [Add Features](https://developers.arcgis.com/rest/services-reference/add-features.htm)
        
        
   * **Add Features from SDE - v2  |  25,261 Records**
        * Adds features in 4,000 grouped record sets
        * Utilizes [Add Features](https://developers.arcgis.com/rest/services-reference/add-features.htm)
        
        
   * **Append Data |  104,265 Records**
        * Adds features in 50,000 grouped record sets through File geodatabases
        * Utilizes [Append](https://developers.arcgis.com/rest/services-reference/append-feature-service-.htm)
        
        
        
   * **Overwrite Content Using Service Definitions |  548,000 Records**
        * Converts entire dataset into a service definition. Overwrites service. 
        
        * Utilizes [Service Definitions](http://enterprise.arcgis.com/en/server/latest/publish-services/windows/about-service-definition-files.htm)
        
        
        
Although I am connecting to an Enterprise Geodatabase.  The workflows will work just fine with a file geodatabase.
        
## Built With

* [PythonAPI](https://developers.arcgis.com/python/) - Esri Web GIS Library
* [ArcPy](https://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-arcpy-.htm) - Esri Desktop Geoprocessing
* [Jupyter Notebooks](https://jupyter.org/) - Open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.

## Authors

**Alexander Brown | Solution Engineer** 

Esri | 1325 Morris Drive, Suite 201 | Chesterbrook, PA 19087 | USA

T 610 644 3374 x5907 | M 267 361 4779 | alexander_brown@esri.com | esri.com
 
THE SCIENCE OF WHERE ®

## License

This project is public.

## Acknowledgments

* Esri ArcGIS Python API Team
* Esri arcpy Developers
* Harrisburg University
