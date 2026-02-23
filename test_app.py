import os
import requests

def test_environment():
    env = os.environ.get("Environment")
    print("Environment:", env)
    assert env is not None

def test_suite():
    suite = os.environ.get("TestSuite")
    print("Test Suite:", suite)
    assert suite in ["smoke", "regression"]

def test_dummy():
    # Example external test (replace with actual endpoint later)
    print("Running external test validation")
    assert True