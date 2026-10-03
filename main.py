"""MP3 Tag Edit — Edit title, artist, and album tags on a folder of mp3 files."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='mp3_tag_edit',
        description='Edit title, artist, and album tags on a folder of mp3 files.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('MP3 Tag Edit')
    print('ID3 tags without a heavy library app.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
