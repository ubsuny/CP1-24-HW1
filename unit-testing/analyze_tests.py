#TODO:  Temporarily, I've assumed a default tolerance value of 0.05 for the sake of
#       defining test cases across a consistent range. The default value should be
#       reassessed later on.

#TODO:  clean up test responses

# import the math module
import math

# this function will be run against each test case. it compares the expected probability
# with a test case's meaured probability to determine whether or not it falls
# withing the acceptable range of tolerance.
def analyze_chsh_result(counts, expected_probabilities, shots, tolerance=0.05):
    """
    Compare raw counts to expected probabilities and print the result of the analysis.

    Args:
        counts (dict): Measurement results from the circuit.
        expected_probabilities (dict): The expected probabilities for each outcome.
        shots (int): Total number of measurements taken.
        tolerance (float): Allowed deviation from the expected probability.
    """
    for outcome, count in counts.items():
        measured_prob = count / shots
        expected_prob = expected_probabilities.get(outcome, 0)

        if math.isclose(measured_prob, expected_prob, abs_tol=tolerance):
            print(f"Test passed for outcome {outcome}: Measured {measured_prob:.4f}, Expected {expected_prob:.4f}.")
            print(f"[PASS]\t Yay!--  The outcome is inside the range of expected values.")
        else:
            print(f"Test failed for outcome {outcome}: Measured {measured_prob:.4f}, Expected {expected_prob:.4f}.")
            print(f"[FAIL]\t Oops-- The outcome is outside the range of expected values.")
def analyze_chsh_tests(test_cases):
    """
    Analyze the test cases and output results.

    Args:
        test_cases (list): List of test cases to analyze.
    """
    # get the total number of tests prepared
    total_tests_count = len(test_cases)

    # Define expected probabilities for the outcomes
    expected_probabilities = {
        '00': 0.5,
        '11': 0.5,
        # You can add more outcomes if your test cases involve other measurements
    }

    # Loop through the test cases and analyze each one
    for test_case in test_cases:
        # get the test number
        current_test_number = test_cases.index(test_case)

        # prepare some objects to be analyzed
        angles = test_case['angles']
        counts = test_case['counts']
        shots = test_case['shots']

        # announce what test is about to be run (and total testing progress)
        print(f"\n[{current_test_number+1}/{total_tests_count}] Analyzing test for angles: {angles}")
        # run an analysis on this test
        analyze_chsh_result(counts, expected_probabilities, shots)
