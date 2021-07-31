# a setup file for pypi packages and librabry


# Third Party
from setuptools import setup




with open('README.md') as readme:
    long_description = readme.read()

# with open('requirements.txt') as requirements_production:
#     install_requires = requirements_production.readlines()

setup(
    name='tzunipy',

    description='A python package that provides details about Universities of Tanzania',

    long_description=long_description,

    long_description_content_type='text/markdown',

    version='0.1',    # keep on changing

    url='https://github.com/maen08/tzunipy',

    download_url='https://github.com/ioi2908/djangoroku/archive/v_01.tar.gz',

    author='Stanley Ruheza',

    author_email='2001stany@gmail.com',

    license='MIT',

    packages=['tzunipy'],

    include_package_data=True,

    install_requires= [ 'setuptools'],

    keywords=['tanzania', 'university', 'tanzania-university', 'unipy' , 'tz'],

    classifiers=[
       
        'Development Status :: 3 - Alpha',  # keep on increasing
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.x',
    ],

    

)
