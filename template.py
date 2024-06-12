import os
from pathlib import Path


package_name = "mangodb_connect"

list_of_files = [
".github/workflows/ci.yaml",
f"src/{package_name}/__init__.py",
f"src/{package_name}/mongo_crud.py",
"tests/unit/__init__.py",
"tests/unit/unit.py",
"tests/integration/integration.py",
"pyproject.toml",
"setup.py",
"setup.cfg",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"experiment/experiment.ipynb",
"tox.ini"
]




for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok = True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
