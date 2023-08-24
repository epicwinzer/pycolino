from pycolino import prepare_options, create_read, create_write
import pytest


def test_prepare_options():
    assert prepare_options("a", "b") == ("a", "b", "write")
    assert prepare_options("a", "") == ("a", "", "read")
    assert prepare_options("", "") == ("", "", "default")
    assert prepare_options("", "b") == ("", "b", "default")


def test_create_read():
    # case 1: file is in list, message as well
    temp_dr = [{"name": "hello", "message": "world"}, {"name": "CS", "message": ""}]
    selected_file = "hello"
    assert create_read(temp_dr, selected_file) == [
        {"name": "hello", "message": "world"}
    ]

    # case 2: file is in list, but blank message
    selected_file = "CS"
    assert create_read(temp_dr, selected_file) == [{"name": "CS", "message": ""}]

    # case 3: file is not in list
    selected_file = "foobar"
    with pytest.raises(SystemExit):
        assert create_read(temp_dr, selected_file)


def test_create_write():
    # case 1: file in list, overwrite message
    temp_dr = [{"name": "hello", "message": "world"}, {"name": "CS", "message": ""}]
    selected_file = "hello"
    phrase = "This is CS50!"
    assert create_write(temp_dr, selected_file, phrase) == [
        {"name": "hello", "message": "This is CS50!"}
    ]

    # case 2: file in list, new message
    selected_file = "CS"
    assert create_write(temp_dr, selected_file, phrase) == [
        {"name": "CS", "message": "This is CS50!"}
    ]

    # case 3: file is not in list
    selected_file = "foobar"
    with pytest.raises(SystemExit):
        assert create_write(temp_dr, selected_file, phrase)
