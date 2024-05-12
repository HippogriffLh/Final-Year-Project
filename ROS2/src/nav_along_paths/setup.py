from setuptools import setup

package_name = 'nav_along_paths'
submodule = 'nav_along_paths/submodules'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodule],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hippogriff',
    maintainer_email='Zeren_ZHOU@126.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'nav_along_paths = nav_along_paths.nav_through_poses: main'
        ],
    },
)
