## devops-automation
DevOps Automation Scripts to automate certain tasks on the AWS Cloud Platform.

## General
Scripts can be found under their respected folders. For example all Python scripts will be in the Python folder and all Bash scripts will be in the bash folder. Also note that you have to configure your AWS cli/sdk access accordingly or whichever cloud platform that you make use of ie GCP, Openstack etc.

## SCRIPTS:

### ami_cleanup_30days.py
Deregister/delete all ami images on AWS older than 30 days.

### ami_cleanup_3versions.py
Deregister/delete all ami images on AWS older than 3 versions. Only the 3 latest versions will remain
