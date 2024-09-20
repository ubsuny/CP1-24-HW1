#TODO:  The next stage of this file should prepare test cases using actual
#       output data from the circuit.

#TODO:  Determine where in the project structure output data should live

#TODO: Add exception handling once we start using nontrivial test cases
#      -especially for handling data/file importing

#TODO:  Temporarily, I've assumed a default tolerance value of 0.05 for the sake of
#       defining test cases across a consistent range. The default value should be
#       reassessed later on.


def prepare_test_cases():
    """
    Create a list of tests that will be returned. First some passing cases are
    prepared and added to the list, then some failing cases are prepared and added.

    To test additional cases, add them to test_cases (a list of test cases)

    Returns:
        list of dicts: a list of the prepared test cases, each case a single dict
    """
    test_cases = []

    passing_test_cases = prepare_passing_test_cases()   # get the passing cases as a list
    failing_test_cases = prepare_failing_test_cases()   # get the failing cases as a list

    # Add the passing and failing test cases to the list of tests to be analyzed
    test_cases.extend(passing_test_cases)
    test_cases.extend(failing_test_cases)

    return test_cases   # return the full list of prepared test cases


# Lets start by creating some test cases that should pass due to equality
# or are very close in terms deviation from the expected value, which for
# now we will assume is .05 (or 5%).
def prepare_passing_test_cases():
    """
    Prepare test cases that will pass the unit test for the CHSH inequality.
    These test cases have raw outputs close to the expected probabilities. If
    any of these cases fail using a tolerance value of .05, analyze_tests.py
    should be inspected for errors.
    """
    passing_test_cases = []

    # Test case 1: angles (0, 0), expected 50% for '00' and '11'
    test_case_1 = {
        'angles': (0, 0),
        'counts': {'00': 512, '11': 512},  # 50% '00' and 50% '11' for 1024 shots
        'shots': 1024
    }
    passing_test_cases.append(test_case_1)

    # Test case 2: angles (0, 45), slight deviation but within tolerance
    test_case_2 = {
        'angles': (0, 45),
        'counts': {'00': 500, '11': 500},  # 48.8% '00', 48.8% '11', within tolerance
        'shots': 1024
    }
    passing_test_cases.append(test_case_2)

    # Test case 3: angles (45, 90), slightly more deviation, still within tolerance
    test_case_3 = {
        'angles': (45, 90),
        'counts': {'00': 510, '11': 514},  # 49.8% '00', 50.2% '11'
        'shots': 1024
    }
    passing_test_cases.append(test_case_3)

    # Test case 4: angles (90, 135), valid outcome
    test_case_4 = {
        'angles': (90, 135),
        'counts': {'00': 480, '11': 544},  # 46.8% '00', 53.2% '11', within tolerance
        'shots': 1024
    }
    passing_test_cases.append(test_case_4)

    return passing_test_cases

# Now let's write some test cases that should fail.
def prepare_failing_test_cases():
    """
    Prepare test cases that will fail the unit test for the CHSH inequality.
    These test cases have raw outputs that deviate beyond the expected probabilities.
    If any of these cases pass using a tolerance of .05, analyze_tests should
    be inspected for errors.
    """
    failing_test_cases = []

    # Test case 1: angles (0, 0), counts deviate beyond tolerance
    test_case_1 = {
        'angles': (0, 0),
        'counts': {'00': 600, '11': 424},  # Significant deviation from 50% '00', '11'
        'shots': 1024
    }
    failing_test_cases.append(test_case_1)

    # Test case 2: angles (0, 45), more significant deviation
    test_case_2 = {
        'angles': (0, 45),
        'counts': {'00': 700, '11': 300},  # Far from expected 50-50 distribution
        'shots': 1024
    }
    failing_test_cases.append(test_case_2)

    # Test case 3: angles (45, 90), another major deviation
    test_case_3 = {
        'angles': (45, 90),
        'counts': {'00': 100, '11': 900},  # Very skewed toward '11', should fail
        'shots': 1024
    }
    failing_test_cases.append(test_case_3)

    # Test case 4: angles (90, 135), extreme deviation
    test_case_4 = {
        'angles': (90, 135),
        'counts': {'00': 0, '11': 1024},  # No '00' at all, extreme case
        'shots': 1024
    }
    failing_test_cases.append(test_case_4)

    return failing_test_cases
