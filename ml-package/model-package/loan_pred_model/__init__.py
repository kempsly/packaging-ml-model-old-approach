import os
from loan_pred_model.config import config 
with open(os.path.join(config.PACKAGE_ROOT, "VERSION")) as v_file:
    __version__ = v_file.read().strip()