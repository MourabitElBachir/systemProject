from systemadmin.files import File
from configparser import ConfigParser
import os
from utils.utils import Root

def test_typeoffile():
    config = ConfigParser()
    config.read(os.path.join(Root.get_project_root(), 'configfile.properties'))

    file1 = File(os.path.join(Root.get_project_root(), config['resources']['file.1']))
    file2 = File(os.path.join(Root.get_project_root(), config['resources']['file.2']))
    file3 = File(os.path.join(Root.get_project_root(), config['resources']['file.3']))

    assert file1.typeoffile() == "standard file"
    assert file2.typeoffile() == "dir"
    assert file3.typeoffile() == "not a file"
