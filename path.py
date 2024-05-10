import os

TMP_PATH=".tmp"
OUT_PATH="result"

def ensure_tmp_path(video):
    name = video['qualified_name']

    # Ensure the out directory exists
    if not os.path.exists(TMP_PATH):
        os.makedirs(TMP_PATH)

        # Ensure the tmp directory for this video exists
    if not os.path.exists(f'{TMP_PATH}/{name}'):
        os.makedirs(f'{TMP_PATH}/{name}')

def ensure_out_path(video):
    name = video['qualified_name']

    # Ensure the out directory exists
    if not os.path.exists(OUT_PATH):
        os.makedirs(OUT_PATH)

        # Ensure the tmp directory for this video exists
    if not os.path.exists(f'{OUT_PATH}/{name}'):
        os.makedirs(f'{OUT_PATH}/{name}')