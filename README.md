# Solving Regression Problem Using Neural Network

## solve with "sklearn code"

-  step1

  install scikit-learn:

  scikit-learn requires:

  - Python (>= 3.6)
  - NumPy (>= 1.13.3)
  - SciPy (>= 0.19.1)
  - joblib (>= 0.11)
  - threadpoolctl (>= 2.0.0)

  If you already have a working installation of numpy and scipy, the easiest way to install scikit-learn is using `pip`

  `$ pip install -U scikit-learn`

  or `conda`:

  `$ conda install -c conda-forge scikit-learn`

-  step2

  We use the prepare.py to correct the structure of the excel files:

  `$ python prepare.py data_1.csv data_1_out.csv 4 1`

  `$ python prepare.py data_2.csv data_2_out.csv 4 1`

-  step3

  Run the code on dataset number 1:

  `$ python3 solve_1.py`

  Run the code on dataset number 2:

  `$ python3 solve_2.py`

## solve with "keras code"

 If u want run the code on dataset number 1:

​		`$ python3 keras_1.py`

 else for dataset number 2 open the keras_1.py and change

 df = pandas.read_csv("data_1_out.csv") to df = pandas.read_csv("data_2_out.csv") 

 and save the file then:

​	  `$ python3 keras_1.py`



