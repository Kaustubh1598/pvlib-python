
from nose.tools import *
import numpy as np
import pandas as pd 
from .. import pvl_relativeairmass

def test_proper():
	AM=pvl_relativeairmass.pvl_relativeairmass(z=5)
	AM2=pvl_relativeairmass.pvl_relativeairmass(z=5,model='kastenyoung1989')
	print AM
	print AM2
	assert(AM==AM2)

	#include physical checks
@raises(Exception)
def test_fail():
	AM=pvl_relativeairmass.pvl_relativeairmass(z=600)
	assert(AM>0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()