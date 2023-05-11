import os
import pypandoc
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Azure Blob Storage connection string for the source container
src_connection_string = "DefaultEndpointsProtocol=https;AccountName=<source_account_name>;AccountKey=<source_account_key>;EndpointSuffix=core.windows.net"

# Azure Blob Storage connection string for the destination container
dst_connection_string = "DefaultEndpointsProtocol=https;AccountName=<destination_account_name>;AccountKey=<destination_account_key>;EndpointSuffix=core.windows.net"

# Define the names of the source and destination containers
src_container_name = "my-source-container"
dst_container_name = "my-destination-container"

# Convert a markdown file to a PDF
def convert_markdown_file(file_path):
    # Use pypandoc to convert the markdown file to a PDF
    output_file = file_path[:-3] + 'pdf'
    pypandoc.convert_file(file_path, 'pdf', outputfile=output_file)

    return output_file

# Search for markdown files in the source container and convert them to PDFs
def process_markdown_files():
    # Create a BlobServiceClient for the source container
    src_blob_service_client = BlobServiceClient.from_connection_string(src_connection_string)
    src_container_client = src_blob_service_client.get_container_client(src_container_name)

    # Create a BlobServiceClient for the destination container
    dst_blob_service_client = BlobServiceClient.from_connection_string(dst_connection_string)
    dst_container_client = dst_blob_service_client.get_container_client(dst_container_name)

    # List all blobs in the source container
    blob_list = src_container_client.list_blobs()

    # Filter the list of blobs to only include markdown files
    markdown_files = [blob.name for blob in blob_list if blob.name.endswith('.md')]

    # Convert each markdown file to a separate PDF and upload it to the destination container
    for file in markdown_files:
        # Download the markdown file from the source container
        src_blob_client = src_container_client.get_blob_client(file)
        file_path = os.path.basename(file)
        with open(file_path, "wb") as data:
            data.write(src_blob_client.download_blob().readall())

        # Convert the markdown file to a PDF
        pdf_file = convert_markdown_file(file_path)

        # Upload the PDF file to the destination container
        with open(pdf_file, "rb") as data:
            dst_blob_client = dst_container_client.get_blob_client(pdf_file)
            dst_blob_client.upload_blob(data)

        # Delete the temporary markdown and PDF files
        os.remove(file_path)
        os.remove(pdf_file)

if __name__ == "__main__":
    process_markdown_files()
