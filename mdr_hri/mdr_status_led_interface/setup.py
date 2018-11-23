#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['mdr_status_led_interface'],
    package_dir={'mdr_status_led_interface':
                 'ros/src/mdr_status_led_interface'}
)

setup(**d)
