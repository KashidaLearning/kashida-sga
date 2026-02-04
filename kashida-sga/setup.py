"""
Setup for Kashida Staff Graded Assignment XBlock.
"""
import os

from setuptools import find_packages, setup

import kashida_sga


def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root_list`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))
    return {pkg: data}


setup(
    name="kashida-sga",
    version=kashida_sga.__version__,
    description="Kashida Staff Graded Assignment XBlock",
    license="GNU Affero General Public License v3 or later (AGPLv3+)",
    url="https://github.com/kashida-learning/kashida-sga",
    author="Kashida",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Education",
    ],
    install_requires=[
        "XBlock",
        "xblock-utils",
        "web_fragments",
    ],
    entry_points={
        "xblock.v1": [
            "kashida_staffgradedassignment = kashida_sga.sga:KashidaStaffGradedAssignmentXBlock",
        ]
    },
    package_data=package_data("kashida_sga", ["static", "templates"]),
)
