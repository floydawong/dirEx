# DirEx
> An extension to the built-in function dir() for Python  


## APIs
- show_dir_info
- show_dir_method
- show_dir_module


## Install
`pip install direx`


## Example
```Python
from direx import show_dir_info, show_dir_method, show_dir_module

import os

show_dir_module(os)
show_dir_method(os)
show_dir_info()
```
