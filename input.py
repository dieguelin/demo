import pandas as pd

import json
import os
import pickle
import sys


def get_input(local=False):
    if local:
        print("Reading local file dataset.csv")
        return "dataset.csv"

    dids = os.getenv("DIDS", None)

    if not dids:
        print("No DIDs found in environment. Aborting.")
        return

    dids = json.loads(dids)

    for did in dids:
        filename = f"data/inputs/{did}/0"  # 0 for metadata service
        print(f"Reading asset file {filename}.")

        return filename


def run_algo(local=False):
    filename = get_input(local)
    if not filename:
        print("Could not retrieve filename.")
        return

    df = pd.read_csv(filename)

    # Number 1
    number_1 = df.iloc[0]
    # Number 2
    number_2 = df.iloc[1]

    # Add two numbers
    results = number_1 + number_2

    filename = "results.pickle" if local else "/data/outputs/result"
    with open(filename, "wb") as pickle_file:
        print(f"Pickling results in {filename}")
        pickle.dump(results, pickle_file)


if __name__ == "__main__":
    local = len(sys.argv) == 2 and sys.argv[1] == "local"
    run_algo(local)
