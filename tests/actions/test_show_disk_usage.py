import pytest
from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path


@pytest.fixture
def file_context(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("File content")
    file2 = tmp_path / "file2.txt"
    file2.write_text("Another file content")
    return {"all_files": [str(file1), str(file2)]}


def test_show_disk_usage_with_files(capsys, file_context):
    file_test1 = f"'{_get_printable_file_path(file_context['all_files'][0])}':"
    file_test2 = f"'{_get_printable_file_path(file_context['all_files'][1])}':"
    show_disk_usage(file_context)
    captured = capsys.readouterr()
    assert captured.out == (
        f"{file_test2.ljust(70)} 20 (62%)\n" +
        f"{file_test1.ljust(70)} 12 (37%)\n" +
        f"Total size: {32}\n"
    )


def test_show_disk_usage_no_files(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"
