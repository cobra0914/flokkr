
from jinja2 import Environment, FileSystemLoader
import os

class Template:

   def __init__(self, basedir):
        self.basedir = basedir

   def transform_content(self, filepath, content):
       t = Environment(loader=FileSystemLoader(os.path.dirname(filepath))).from_string(content)
       return t.render(env = os.environ)