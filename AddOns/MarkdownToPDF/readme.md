This script uses the pypandoc library to convert each markdown file to a separate PDF file, with one PDF file per page. This will allow your to pull your markdown files from places like Github and use them within Azure OpenAI. The resulting PDF files are uploaded to the destination container using the Azure Blob Storage SDK, and the original markdown files are deleted from the source container. 

You will need to replace the placeholders in the connection strings and container names with your actual values.

How to find the Storage Account connection string:
![image](https://github.com/DarrenTurchiarelli/azure-search-openai-demo/assets/107463700/411eb9b4-68d7-4105-9223-e9b6900e3021)
