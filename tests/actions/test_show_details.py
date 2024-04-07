import pytest
import os
from datetime import date
from pro_filer.actions.main_actions import show_details


@pytest.fixture
def file_exists_context(tmp_path):
    # Criação de um arquivo dentro do diretório temporário
    file_path = tmp_path / "pro-filer-preview.gif"
    file_path.write_text("File content")
    return {"base_path": str(file_path)}


@pytest.fixture
def file_not_exists_context():
    return {"base_path": "/home/trybe/???"}


@pytest.fixture
def file_without_extension_context(tmp_path):
    # Criação de um diretório dentro do diretório temporário
    dir_path = tmp_path / "images"
    os.mkdir(dir_path)
    return {"base_path": str(dir_path)}


def test_show_details_file_exists(capsys, file_exists_context):
    show_details(file_exists_context)
    captured = capsys.readouterr()
    assert captured.out == (
        "File name: pro-filer-preview.gif\n"
        "File size in bytes: 12\n"  # Tamanho do conteúdo do arquivo
        "File type: file\n"
        "File extension: .gif\n"
        f"Last modified date: {date.today()}\n"
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
        "File size in bytes: 4096\n"  # Tamanho de um diretório vazio
        "File type: directory\n"
        "File extension: [no extension]\n"
        f"Last modified date: {date.today()}\n"
    )
