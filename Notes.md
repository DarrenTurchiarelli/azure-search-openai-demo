
Install the Azure Developer CLI (preview). 
Source: http://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd

Windows install command: powershell -ex AllSigned -c "Invoke-RestMethod 'https://aka.ms/install-azd.ps1' | Invoke-Expression"


## Deployment

To initially deploy resource run: azd deploy

Once you have updated any resources and plan on redeploying, you will need to run: azd provision or azd up

