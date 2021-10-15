# If you want a method accessable when you import the package name, i.e.
# `mypackage` you will need to import it here

# now if you import, `mypackage` you can call `my_method` using, `mypackage.my_method`.
from .mymodule import my_method
