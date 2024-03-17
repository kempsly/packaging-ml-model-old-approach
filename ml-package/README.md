#### Packaging model

To execute the package without any installation just use this command in your terminal:

setx PYTHONPATH=%PYTHONPATH%;C:\Users\Administrator\Kempsly\Documents\packaging-ml-model-old-approach\ml-package\model-package

<!-- Make sure to replace kempsly by your own user name, that is for windows user -->

## Important Note
To resolve: ModuleNotFoundError: No module named 'loan_pred_model'
 For some reason, any imports in the form of "from prediction_model.xx import yy" were failing with the " No module named 'prediction_model'" error. You could  resolve this by removing loan_pred_model from the path. So, now all the imports that refer to a package under loan_pred_model, you could directly import the packages. For example, rather than "import processing.preprocessing as pp", I do "import preprocessing as pp".

Also, in config.py, I removed references to loan_pred_model and got the PACKAGE_ROOT like below. The training_pipeline now runs and generates and saves the model.

    current_directory = os.path.dirname(os.path.realpath(__file__))
    PACKAGE_ROOT = os.path.dirname(current_directory)