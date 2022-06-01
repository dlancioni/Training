https://docs.python.org/3/library/unittest.html

Lines below are used to allow src/test folder structure below
    import sys
    sys.path.append("..")

Considering the folder structure below
    project
    |___src
    |___test

# [ALL TESTS] from root (project), run the test class (-s indicate the test folder)

    python -m unittest discover -stest -v

# [EACH TEST] Enter the /test folder

    # Run each test class
    python -m unittest test_sum.py -v
    python -m unittest test_sub.py -v

    # run all test files in the same folder
    python -m unittest discover -v 

