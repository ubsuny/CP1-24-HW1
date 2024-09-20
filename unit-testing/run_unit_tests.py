# import the object that will prepare the test cases
from prepare_tests import prepare_test_cases

# import the object that will analyze the test cases
from analyze_tests import analyze_chsh_tests

# retrieve the test cases
def run_chsh_tests():
    """
    Retrieve predefined test cases from raw output.

    Returns:
        test_cases: a list of the prepared test cases, each case a dict
    """
    test_cases = prepare_test_cases()       # prep the test cases
    return test_cases                       # return them to the caller

# anayze the outcome of the tests
def run_and_analyze_tests():
    """
    Run the CHSH tests and analyze the results.
    """
    # get the prepared list of test cases
    test_cases = run_chsh_tests()

    # call the analyzer to process the results
    analyze_chsh_tests(test_cases)

if __name__ == "__main__":          # if this module was executed directly
    run_and_analyze_tests()         # then proceed to run and analyze the tests
