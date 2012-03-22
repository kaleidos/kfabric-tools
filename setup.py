from setuptools import setup, find_packages

description="Kaleidos Fabric Plugins (Tools)"
long_description = ""

setup(
    name="kfabric-tools",
    version=':versiontools:kfabric:',
    url='https://github.com/kaleidos/kfabric-tools',
    license='BSD',
    platforms=['OS Independent'],
    description = description.strip(),
    long_description = long_description.strip(),
    author = 'Andrei Antoukh',
    author_email = 'niwi@niwi.be',
    maintainer = 'Andrei Antoukh',
    maintainer_email = 'niwi@niwi.be',
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'distribute',
        'fabric',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    zip_safe = False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
