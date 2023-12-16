from setuptools import find_packages, setup

package_name = 'samis_drone_crl'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='peteraerocedi',
    maintainer_email='abosedepeter13@gmail.com',
    description='Drone Initial Controls',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'initiate = samis_drone_crl.initiate_drone:tello_node',
        ],
    },
)
