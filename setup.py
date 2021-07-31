# a setup file for pypi packages and librabry


# Third Party
from setuptools import setup




with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements_production:
    install_requires = requirements_production.readlines()

setup(
    name='',

    description='',

    long_description=long_description,

    long_description_content_type='text/markdown',

    version='',    # keep on changing

    url='https://github.com/maen08/',

    download_url='https://github.com/ioi2908/djangoroku/archive/v_01.tar.gz',

    author='',

    author_email='2001stany@gmail.com',

    license='MIT',

    packages=[''],

    include_package_data=True,

    install_requires=install_requires,

    keywords=['django', 'heroku', 'deploy django', 'django heroku'],

    classifiers=[
       
        'Development Status :: 3 - Alpha',  # keep on increasing
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    

)
