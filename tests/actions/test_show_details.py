import pytest
from pro_filer.actions.main_actions import show_details


@pytest.fixture
def file_exists_context():
    return {"base_path": "images/pro-filer-preview.gif"}


@pytest.fixture
def file_not_exists_context():
    return {"base_path": "/home/trybe/???"}


@pytest.fixture
def file_without_extension_context():
    return {"base_path": "images"}


def test_show_details_file_exists(capsys, file_exists_context):
    show_details(file_exists_context)
    captured = capsys.readouterr()
    assert captured.out == (
        "File name: pro-filer-preview.gif\n"
        "File size in bytes: 270824\n"
        "File type: file\n"
        "File extension: .gif\n"
        "Last modified date: 2024-03-28\n"
    )


def test_show_details_file_not_exists(capsys, file_not_exists_context):
    show_details(file_not_exists_context)
    captured = capsys.readouterr()
    assert captured.out == (
        "File '???' does not exist\n"
    )


def test_show_details_file_without_extension(
        capsys, file_without_extension_context):
    show_details(file_without_extension_context)
    captured = capsys.readouterr()
    assert captured.out == (
        "File name: images\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        "Last modified date: 2024-03-28\n"
    )
