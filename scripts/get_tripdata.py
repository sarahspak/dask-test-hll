import shutil
import urllib.request
import os
import zipfile
import argparse

"""Downloads Citibike trip data as zip files then unzips them.
Downloads NY trip data for June 2013 to May 2021 and NJ trip data for September 2015 to May 2021 (as of June 28, 2021).
Adapted from: https://github.com/cl2871/citibike/blob/1f06bda07235929c4d3ca7c8f0a7d22300c55445/citibike_python/get_tripdata.py
"""


def retrieve_citibike_data(start_year=2013, end_year=2021, target="data/citibike_trips_nyc/"):
    """Retrieves trip data from Citibike's S3 buckets as zip files.
    Downloads trip data, default from June 2013 to May 2021
    Returns:
        Nothing
    """

    for year in range(start_year, end_year):
        for month in range(1, 13):

            date_format = str(year) + '{:02d}'.format(month)
            print(date_format)
            # retrieve data from citibike's s3 buckets and store in zip directory
            # weird change in zip naming convention before 2017
            if year < 2017:
                urllib.request.urlretrieve("https://s3.amazonaws.com/tripdata/" + date_format +
                                           "-citibike-tripdata.zip", target + date_format + "-citibike-tripdata.zip")
            else:
                urllib.request.urlretrieve("https://s3.amazonaws.com/tripdata/" + date_format +
                                           "-citibike-tripdata.csv.zip", target + date_format + "-citibike-tripdata.zip")
            print(str(year) + "-" + str(month) + " done")
            

def retrieve_citibike_jc_data(start_year_JC=2015, end_year_JC=2021, target="data/citibike_trips_JC/"):

    """Does same thing as retrieve_citibike_data() but for Jersey City data
    Downloads trip data from September 2015 to December 2017.
    """

    for year in range(start_year_JC, end_year_JC):
        for month in range(1, 13):
            date_format = str(year) + '{:02d}'.format(month)

            # retrieve data from citibike's s3 buckets and store in zip directory
            # note: JC-201708 is missing a dash
            if year == 2017 and month == 8:
                urllib.request.urlretrieve(
                    "https://s3.amazonaws.com/tripdata/JC-" + date_format + " citibike-tripdata.csv.zip" + ".csv.zip", 
                    target + date_format + "-citibike-tripdata.zip")
            else:
                urllib.request.urlretrieve(
                    "https://s3.amazonaws.com/tripdata/JC-" + date_format + "-citibike-tripdata.csv.zip" + ".csv.zip",
                    target + date_format + "-citibike-tripdata.zip")
            print(str(year) + "-" + str(month) + " done")


def unzip_citibike_data(zip_dir):

    """Unzips Citibike zip files
    Returns:
        Nothing
    """
#     zip_dir = "data/citibike-tripdata-nyc/"
#     csv_dir = "data/citibike-tripdata-nyc/csv"
    extension = ".zip"

    # for each zip file in zip_dir extract data
    for item in os.listdir(zip_dir):
        if item.endswith(extension):

            # create zipfile object and extract
            file_name = zip_dir + item
            with zipfile.ZipFile(file_name, "r") as zip_ref:
                zip_ref.extractall(zip_dir)
                print(item + " done")

def main(start_year=2013, end_year=2021, start_year_JC=2015, end_year_JC=2021):
    retrieve_citibike_data(start_year, end_year)
    retrieve_citibike_jc_data(start_year_JC, end_year_JC)
    unzip_citibike_data()

                
if __name__ == "__main__":
    main(start_year=2013, end_year=2021, start_year_JC=2015, end_year_JC=2021)
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--start_year', dest='start_year', type=int, nargs='+',
#                     help='start year for NYC citibike data')
#     parser.add_argument('--end_year', dest='end_year', type=int, nargs='+',
#                     help='end year for NYC citibike data')
#     parser.add_argument('--start_year_JC', dest='start_year_JC', type=int, nargs='+',
#                     help='start year for JC citibike data')
#     parser.add_argument('--end_year_JC', dest='end_year_JC', type=int, nargs='+',
#                     help='end year for JC citibike data')

#     args = parser.parse_args()
    

#     retrieve_citibike_data(start_year, end_year)
#     retrieve_citibike_jc_data(start_year_JC, end_year_JC)
#     unzip_citibike_data()
