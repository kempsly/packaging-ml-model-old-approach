#### Packaging model

To execute the package without any installation just use this command in your terminal:
`set PYTHONPATH=%PYTHONPATH%;C:\Users\Administrator\Kempsly\Documents\packaging-ml-model-old-approach\ml-package\model-package`

<!-- set PYTHONPATH=%PYTHONPATH%;C:\Users\Administrator\Kempsly\Documents\packaging-ml-model-old-approach\jenkins-cicd-ml\src -->
<!-- set PYTHONPATH=%PYTHONPATH%;c:\users\kempsly\anaconda3\envs\venvjenkins\lib\site-packages -->

<!-- To make it permanetly -->
`setx PYTHONPATH "%PYTHONPATH%;C:\Users\Administrator\Kempsly\Documents\packaging-ml-model-old-approach\ml-package\model-package"`

`setx PYTHONPATH "%PYTHONPATH%;CUsers\Administrator\Kempsly\Documents\packaging-ml-model-old-approach\ml-package\model-package"`

<!-- Make sure to replace kempsly by your own user name, that is for windows user -->

## Important Note
To resolve: ModuleNotFoundError: No module named 'loan_pred_model':

 1. For some reason, any imports in the form of "from loan_pred_model.xx import yy" were failing with the " No module named 'loan_pred_model'" error. You could  resolve this by removing loan_pred_model from the path. So, now all the imports that refer to a package under loan_pred_model, you could directly import the packages. For example, rather than "import processing.preprocessing as pp", I do "import preprocessing as pp".

Also, in config.py, I removed references to loan_pred_model and got the PACKAGE_ROOT like below. The training_pipeline now runs and generates and saves the model.

    current_directory = os.path.dirname(os.path.realpath(__file__))
    PACKAGE_ROOT = os.path.dirname(current_directory)
    
2. Second approach, this what is recommended: just add this line of code inside the config.py file after defining PACKAGE_ROOT:
ROOT = PACKAGE_ROOT.parent
Leave all the remaining setup as it is.


# Building the package :
1. Create a virtual environnement

2. Install all dependencies using:
  `pip install -r requirements.txt`
  
3. TRaining the model and generating pickle file:
  `python loan_pred_model/training_pipeline.py`
  
4. Create source distribution and wheel:
   `python setup.py sdist bdist_wheel`


# How to install the package
- To install the package run this command in your terminal:
 `pip install git+https://github.com/kempsly/packaging-ml-model-old-approach.git@main#subdirectory=ml-package/model-package`

- another important note, when
  