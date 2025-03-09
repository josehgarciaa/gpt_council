# gpt_council/modules/__init__.py

import pkgutil

# Automatically determine available modules
__all__ = [name for _, name, _ in pkgutil.iter_modules(__path__)]


from .modules import *

# Optionally, if you want the module names to appear in the package namespace:
# This will import each module as an attribute of gpt_council.
import pkgutil
import importlib

modules_path = __path__[0] + '/modules'
for finder, module_name, is_pkg in pkgutil.iter_modules([modules_path]):
    module = importlib.import_module(f"{__name__}.modules.{module_name}")
    globals()[module_name] = module