#! /usr/bin/python3
import io
import logging
import sys
import tempfile

import atheris
import spacy
import warnings

warnings.filterwarnings("ignore")
logging.disable(logging.CRITICAL)

with atheris.instrument_imports():
    from pyresparser import ResumeParser

nlp = spacy.load('en_core_web_sm')


@atheris.instrument_func
def TestOneInput(data):
    fd = io.BytesIO()
    fd.write(data)
    fd.name = 'test.pdf'
    ResumeParser(fd, default_nlp=nlp).get_extracted_data()


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
