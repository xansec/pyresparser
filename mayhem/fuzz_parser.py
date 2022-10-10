#! /usr/bin/python3
import logging
import sys
import tempfile

import atheris

logging.disable(logging.CRITICAL)

with atheris.instrument_imports():
    from pyresparser import ResumeParser


@atheris.instrument_func
def TestOneInput(data):
   with tempfile.NamedTemporaryFile() as f:
       f.write(data)
       f.flush()
       ResumeParser(f.name).get_extracted_data()

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
