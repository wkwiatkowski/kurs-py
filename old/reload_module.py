#!/usr/bin/env python
# The issue refers to an interactive session. 
# Every imported module works once per process. The next module call does not execute it. To do that, a module has to be reload
# to reload module, the module must first be loaded.

import if_statement
from imp import reload

reload(if_statement)
