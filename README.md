The script `extract.py` reads all majors from options in cupt pages http://admission.cuas.or.th/admXXmxmn/

To use the script, add the url prefix for each year.  E.g.,

```
python extract.py adm60maxmn
python extract.py adm59mxmn
python extract.py adm58mxmn
```

Currently the script does not work for admission year 2551 because the returned major html is not well-formed, i.e., the option tags are not closed.

The extracted major data are in `data` directory.

The score extraction from pdf files is done interactively on jupyter notebook `extract-exp.ipynb`.