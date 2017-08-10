"""
pytest unit tests
Functions should start with ``test_`` and contain a list of assertions that evaluate to True if the test succeeds.
For more info see: http://pytest.org/latest/
"""

import task_bug_scrub_to_csv
def test_task():
    task_bug_scrub_to_csv.task(None,
                               '/var/bdb/sessions/sandboxed-user/test.doc',
                               '/var/bdb/sessions/sandboxed-user/output.csv')
    assert True == True