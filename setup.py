from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.call(['python', 'post_install.py'])

setup(
    name="s3_tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "s3-upload=s3_tool.s3_tool:upload_command",
            "s3-download=s3_tool.s3_tool:download_command",
        ],
    },
    author="Manuel Rodriguez Ladron de Guevara",
    author_email="manuelrodriguez@higharc.com",
    description="A tool for uploading and downloading files and folders to/from S3.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/manuelladron/s3_tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': PostInstallCommand,
    },
)