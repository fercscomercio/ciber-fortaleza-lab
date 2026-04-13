from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")     # Análisis estático de estilo [cite: 165]
use_plugin("python.coverage")   # Auditoría de ejecución [cite: 166]
use_plugin("python.distutils")

name = "BioGuard_Inventory"
default_task = "publish"

@init
def set_properties(project):
    # Umbral de rechazo: El build fallará si la cobertura es < 100% [cite: 98, 171]
    project.set_property("coverage_break_build", True)
    project.set_property("coverage_threshold_warn", 100)
    
    # Política de Estilo: El build fallará ante errores de formato PEP8 [cite: 172]
    project.set_property("flake8_break_build", True)
    project.set_property("flake8_verbose_output", True)