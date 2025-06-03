from __future__ import annotations

from pathlib import Path

from secrets import root_path

if __name__ == "__main__":

    _path: Path = root_path / "Obsidian Vaults\\Sandbox"

    print(_path.is_dir())

    for _ in _path.iterdir():
        print(_.name)
