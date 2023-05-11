## Summary:
This script uses the pypandoc library to convert each markdown file to a separate PDF file, with one PDF file per page. This will allow your to pull your markdown files from places like Github and use them within Azure OpenAI. The resulting PDF files are uploaded to the destination container using the Azure Blob Storage SDK, and the original markdown files are deleted from the source container. 

You will need to replace the placeholders in the connection strings and container names with your actual values.

## Pandoc
There is a package installer at [pandoc’s](https://pandoc.org/installing.html) download page. This will install pandoc, replacing older versions, and update your path to include the directory where pandoc’s binaries are installed.

If you prefer not to use the msi installer, we also provide a zip file that contains pandoc’s binaries and documentation. Simply unzip this file and move the binaries to a directory of your choice.

Alternatively, you can install pandoc using Chocolatey:

choco install pandoc
Chocolatey can also install other software that integrates with Pandoc. For example, to install rsvg-convert (from librsvg, covering formats without SVG support), Python (to use Pandoc filters), and MiKTeX (to typeset PDFs with LaTeX):

choco install rsvg-convert python miktex
Or, you can install pandoc using winget:

winget install pandoc

## How to find the Storage Account connection string:
![image](https://github.com/DarrenTurchiarelli/azure-search-openai-demo/assets/107463700/411eb9b4-68d7-4105-9223-e9b6900e3021)
