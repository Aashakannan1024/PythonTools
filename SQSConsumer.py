from urllib.parse import urlparse
from azure.storage.blob import BlobServiceClient


def download_blob_from_url(blob_url, local_file_path, connection_string):
    # Extract container name and blob name from blob URL
    parsed_url = urlparse(blob_url)
    container_name = parsed_url.path.split('/')[1]
    blob_name = '/'.join(parsed_url.path.split('/')[2:])

    # Initialize BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Download the blob to a local file
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(local_file_path, "wb") as local_file:
        blob_data = blob_client.download_blob()
        blob_data.readinto(local_file)

    print(f"Blob {blob_name} has been downloaded to {local_file_path}")


# Example usage
blob_url = "https://cinddvawsblob.blob.core.windows.net/clearcontainer/nmdcUCV2/20230315/others/69225.jpg"
local_file_path = "downloaded_file.mp4"
#connection_string = "DefaultEndpointsProtocol=https;AccountName=cindclearqaawsblob;AccountKey=2YyKWgdF8gHWYwM0n1ed7Tg8q5ogCDkFf77b+T5zMYFF3iFuT9/G8WRd4TsJ/RBRwnlaPhPcNiXjelt/VhtoeQ==;EndpointSuffix=core.windows.net"
connection_string = "DefaultEndpointsProtocol=https;AccountName=cinddvawsblob;AccountKey=vJ/kDue59N0/QIxmlRo2IBRbisaAlLZnosQtUQSjwe0jkwHahfq3KlcFfQ0YYLL6BHmzfmyqVWUZY79dJGAC7g==;EndpointSuffix=core.windows.net";
download_blob_from_url(blob_url, local_file_path, connection_string)
