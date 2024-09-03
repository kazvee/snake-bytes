import sys
import os

project_home = '/home/kazvee/mysite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application