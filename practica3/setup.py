from setuptools import find_packages, setup

package_name = 'practica3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alba',
    maintainer_email='alba.rey@students.salle.url.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'general = practica3.controller:main',
            'talker = practica3.publisher_member_function:main',
            'listener = practica3.subscriber_member_function:main',
        ],
    },
)
