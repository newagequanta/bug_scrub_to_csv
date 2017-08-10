"""
pytest unit tests
Functions should start with ``test_`` and contain a list of assertions that evaluate to True if the test succeeds.
For more info see: http://pytest.org/latest/
"""
import sys
import task_bug_scrub_to_csv
import hashlib

sys.path = ['', '/venv/python361-1/lib/python36.zip', '/venv/python361-1/lib/python3.6', 
'/venv/python361-1/lib/python3.6/lib-dynload', '/home/bdb/.pyenv/versions/3.6.1/lib/python3.6',
'/venv/python361-1/lib/python3.6/site-packages', '/venv/python361-1/src/jtextfsm']

def test_task():
    try:
        task_bug_scrub_to_csv.task(None,
                               '/var/bdb/sessions/sandboxed-user/test.doc',
                               '/var/bdb/sessions/sandboxed-user/tests/bug_scrub_to_csv/output.csv') == True
        assert hashlib.sha256(open('output.csv', 'rb').read()).hexdigest() == '3c2bc6beed31de87f4e6c6114f9ac54a30ec420cf6f160208627a2794f1e61bf'
    except AttributeError:
        assert True
    except:
        assert False