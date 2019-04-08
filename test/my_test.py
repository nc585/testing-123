# testing-123/my_test.py

from app.my_script import enlarge # load the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_enlarge(): # note the function name is prefixed with "test_"
    result = enlarge(3) # directly invoke the function we want to test
    assert result == 9 # describe expectations for desired behavior

#add init file to app directory to be able to show where script comes from 