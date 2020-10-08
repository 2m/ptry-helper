from setuptools import setup
import subprocess

setup(
    name="ptry-helper",
    version=subprocess.check_output(["git", "describe", "--tags", "--long"]).decode("utf8").strip(),
    zip_safe=False,
    include_package_data=True,
    python_requires='>=3.8',
)
