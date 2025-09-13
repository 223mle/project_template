from pathlib import Path

from change_here.env import PROJECT_ROOT


def test_project_root_exists() -> None:
    assert PROJECT_ROOT.exists()
    assert PROJECT_ROOT.is_dir()
    assert isinstance(PROJECT_ROOT, Path)
