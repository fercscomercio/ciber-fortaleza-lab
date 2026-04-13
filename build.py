from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")

name = "bioguard_inventory"
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on('flask')
    project.set_property('dir_source_main_python', 'src/main/python')
    project.set_property('dir_source_unittest_python', 'src/unittest/python')
