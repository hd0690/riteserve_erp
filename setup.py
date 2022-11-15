from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in riteserve_erp/__init__.py
from riteserve_erp import __version__ as version

setup(
	name="riteserve_erp",
	version=version,
	description="Riteserve ERP",
	author="Code Space Techlabs",
	author_email="codespacetechlabs@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
