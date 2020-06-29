import requests
import shutil
import os


FILES = {
    'data': "https://docs.google.com/spreadsheets/d/1gFh5PF4XKoxSSaIxP9E-iZi_xbuyahfAXmhr2j3I1x0/export?format=csv",
    'cases': "https://docs.google.com/spreadsheets/d/1ZrsVqMpQHhBCREc8nluxTA1dJ8lKsGVixgp7JKmfE9I/gviz/tq?tqx=out:csv&sheet=Cases",
    'counties': "https://docs.google.com/spreadsheets/d/1ZrsVqMpQHhBCREc8nluxTA1dJ8lKsGVixgp7JKmfE9I/gviz/tq?tqx=out:csv&sheet=Counties"
}

output_dir="output"


def run():
    ### SETUP OUTPUT FOLDER
    os.makedirs(os.path.join(output_dir), exist_ok=True)

    for filename, url in FILES.items():
        r = requests.get(url, stream=True)
        with open(os.path.join(output_dir, "{}.csv".format(filename)), 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
    print("Complete.")

if __name__ == "__main__":
    run()
