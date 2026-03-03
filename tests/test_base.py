from clean_comments import rewrite_file

from pathlib import Path
def test_basic_1(tmp_path):
    pre = Path("tests/fixtures/pre-clean.py")
    post = Path("tests/fixtures/post-clean.py")

    temp: Path = tmp_path / "del.py"
    temp.write_text(pre.read_text())

    rewrite_file(temp)

    assert temp.read_text() == post.read_text()