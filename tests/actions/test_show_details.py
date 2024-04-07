from pro_filer.actions.main_actions import show_details  # NOQA
import os


def test_show_details_file_exists(capsys):
    context = {
        "base_path": "images/pro-filer-preview.gif"
    }

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        f"File name: {os.path.basename(context['base_path'])}\n"
        "File size in bytes: 270824\n"
        "File type: file\n"
        "File extension: .gif\n"
        "Last modified date: 2024-03-28\n"
    )


def test_show_details_file_not_exists(capsys):
    context = {
        "base_path": "/home/trybe/???"
    }

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        f"File '{os.path.basename(context['base_path'])}' does not exist\n"
    )


def test_show_details_file_without_extension(capsys):
    context = {
        "base_path": "images"
    }

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        f"File name: {os.path.basename(context['base_path'])}\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        f"Last modified date: 2024-03-28\n"
    )
