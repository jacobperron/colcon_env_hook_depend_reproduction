import os


def test_popcorn_env():
    # This should come from package foo
    assert 'POPCORN' in os.environ
