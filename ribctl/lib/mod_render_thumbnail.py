import argparse
import json
import os
import sys
# from pymol import cmd

RIBETL_DATA = str(os.environ.get('RIBETL_DATA'))

def render_thumbnail(pdbid: str):

    pdbid = pdbid.upper()
    thumbnail_path = os.path.join(RIBETL_DATA, pdbid, f"_ray_{pdbid}.png")

    if os.path.exists(thumbnail_path):
        print(f"Thumbnail already exists: {thumbnail_path}")
        sys.exit(0)

    else:
        cmd.load(os.path.join(RIBETL_DATA, pdbid, f"{pdbid}.cif"))
        cmd.reset()
        cmd.spectrum('chain')
        cmd.ray(500, 500)
        cmd.png(thumbnail_path)
        print('Saved {}'.format(thumbnail_path))

if __name__ == "__main__":
    from pymol import cmd, util

    parser = argparse.ArgumentParser(
        description='Generate a ribosome thumbnail image.')
    parser.add_argument("-s", "--structure", type=str,
                        required=True, help="RCSB ID of structure to process")
    args = parser.parse_args()
    pdbid = args.structure.upper()
    thumbnail_path = os.path.join(RIBETL_DATA, pdbid, f"_ray_{pdbid}.png")

    if os.path.exists(thumbnail_path):
        print(f"Thumbnail already exists: {thumbnail_path}")
        sys.exit(0)

    else:
        cmd.load(os.path.join(RIBETL_DATA, pdbid, f"{pdbid}.cif"))
        cmd.reset()
        cmd.spectrum('chain')
        cmd.ray(500, 500)
        cmd.png(thumbnail_path)
        print('Saved {}'.format(thumbnail_path))

