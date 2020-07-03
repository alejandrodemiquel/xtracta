# Exercise: Extract supplier name from invoice

This repository contains the program to extract the supplier name from an invoice.

To execute it straight away, clone the repository, start python in the cloned folder and execute the following commands in python:

```
import exercise
invoice = exercise.read_invoice()
supplier_names = exercise.read_supplier_names()
supplier = exercise.get_supplier_from_invoice(invoice, supplier_names)
```

`supplier` will contain the name of the supplier that appears in the invoice.

<br/><br/>
If you don't want to start python in the cloned folder, you can also start python anywhere and then execute:
```
import os
os.chdir(path_to_cloned_repository)
```

## The exercise module

The file that solves the exercise is exercise.py. It's a python module with three functions:
- `read_invoice(invoice_path)` reads the file containing the information about the invoice given by the input. If no input is given, the function will read the file given for the exercise.
- `read_supplier_names(suppliers_path)` reads the file containing the information about the supplier names given by the input. If no input is given, the function will read the file given for the exercise.
- `get_supplier_from_invoice(invoice, supplier_names)` returns the supplier from the list of suppliers that appears in the invoice.

## Other files

- test.py contains a unit test that tests the correctness of `get_supplier_from_invoice`.
- The folder original_files contais the two .txt files that were originally given for solving the exercise.
- The folder preprocessed_files contains the two preprocessed original files, that I slightly modified in order for them to be read properly by the functions in the exercise module. In particular, invoice is a csv file and supplier_names is a jsonl file. I also added an extra file, fake_suppliers.csv, that I generated in order to test how the algorithm performed with hundreds of thousands of suppliers.
