# Tzunipy

- A python package that gives information about different Universities in Tanzania.
- tzunipy made by [maen08](https://github.com/maen08)



[![Made in Tanzania](https://img.shields.io/badge/made%20in-tanzania-008751.svg?style=flat-square)](https://github.com/Tanzania-Developers-Community/made-in-tanzania)
[![Generic badge](https://img.shields.io/badge/pip-python-<COLOR>.svg)](https://shields.io/)

---

### Install
Run this command to install the current stable version:

`pip install tzunipy`


---

### Features

- [x] Show all universities in Tanzania
- [ ] Shows colleges per university
- [ ] Shows programms pursued per college
- [ ] Shows program duration (if neccessary)

---

### Usage

```sh
>>> from tzuni import TzUniPy


# get all universities

>>> TzUniPy.all_universities()
[
   'University of Dar es Salaam UDSM (Dar es Salaam)', 
   'Sokoine University of Agriculture SUA (Morogoro)', 
   'Open University of Tanzania OUT (Dar es Salaam)', 
    ...
    ...
 
   
]


# get universities from a given region
>>> TzUniPy.get_univeristy('Dodoma')

>>> ['University of Dodoma UDOM (Dodoma)', "St. John's University of Tanzania SJUT (Dodoma)"]


```

### Contribution
- Whoever wish to contribute in this project (direct or indirect), please read 
the file 'update.md'