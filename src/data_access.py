import io
import zipfile
import requests

BASE_URL = (
    "https://www.sec.gov/files/dera/data/"
    "financial-statement-notes-data-sets/"
)

HEADERS = {
    "User-Agent": (
        "Joebin Peter Soosairaj and Shreyas Aravind "
        "EAS587 project joebinpe@buffalo.edu"
    )
}


def download_sec_package(filename):
    url = BASE_URL + filename

    print(f"Accessing SEC package: {filename}")

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=120
    )

    response.raise_for_status()

    return zipfile.ZipFile(io.BytesIO(response.content))


if __name__ == "__main__":
    package = download_sec_package("2026_01_notes.zip")

    print("\nFiles available in the package:")

    for filename in package.namelist():
        print(filename)