# reactions_project

Ignore the incorrect name for the project. 

The following packages will be required. 

pip install pandas
pip install numpy
pip install ploty.express



The project is mainly in the bird_migration_working notebook. All the functions are in the bird_migration_working.py file. 

Explanations for each of the functions can be found in the 'docs' folder in the bird_migration_working_lint.py file

Running in the cells in the jupyter notebook will go through all parts of the project. 

There is one weather file in the repo 'gloti_data.csv' It contains the monthly weather difference until Dec. 2020. 
This can be updated from https://data.giss.nasa.gov/gistemp/ or https://data.giss.nasa.gov/gistemp/tabledata_v4/T_AIRS/GLB.Ts+dSST.csv 

There are 3 example files for birds included in the repo: 
ac_loon.csv = arctic loon
arctic_loon_import.csv = red throated loon (this will be fixed at a later time, as git is clunky with oversized files)
crane.csv = whooping crane

The functions are set up to format csv files from https://www.gbif.org/ specifically for birds but it may work for other biological organisms. 


pytest test_bird_migration_project.py

tests for the type of file that is imported and read by pandas