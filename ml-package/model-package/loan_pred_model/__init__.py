import os
# from loan_pred_model.config import PACKAGE_ROOT, config
from .config import config

# from loan_pred_model.config import config 
# with open(PACKAGE_ROOT / "VERSION") as version_file:
#     __version__ = version_file.read().strip()
    
    
with open(os.path.join(config.PACKAGE_ROOT, "VERSION")) as v_file:
    __version__ = v_file.read().strip()