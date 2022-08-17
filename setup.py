from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gowtham_looms/__init__.py
from gowtham_looms import __version__ as version

setup(
	name="gowtham_looms",
	version=version,
	description="Manufacturing Looms",
	author="Thirvusoft",
	author_email="thirvusoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
