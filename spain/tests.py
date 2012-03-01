#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inquisition import surprise, surprise_file
from inquisition import SURPRISE_MAX_SLEEP_TIME
import time
import sys
import tempfile
import StringIO


def test_surprise():
    """
    tests the surprise method
    """
    saved_stdout = sys.stdout
    fake_stdout = StringIO.StringIO()
    sys.stdout = fake_stdout
    surprise()
    time.sleep(SURPRISE_MAX_SLEEP_TIME +1)
    sys.stdout = saved_stdout
    output = fake_stdout.getvalue()
    assert len(output) > 0
    assert "Nobody" in output

def test_surprise_file():
    """ tests surprise file method
    """
    myfile = tempfile.NamedTemporaryFile()
    surprise_file(myfile.name)
    time.sleep(SURPRISE_MAX_SLEEP_TIME+1)
    output = myfile.readline()
    assert len(output) > 0
    assert "Nobody" in output
    assert "\n" in output #write lines to a file
    # there shouldn't be anything else in the file
    assert len(myfile.readline()) == 0

