# SSM Cloner

## Introduction
---
* This module is created in order to simplify the process of copying the SSM documents from one region to another regions.

* As an organisation or team can have multiple regions in which they operate. And in order to replicate the SSM documents from one region to another.

* It becomes a tedious task if you are developing or if you need to update a document and replicate the change across the regions.

* To resolve this issue, ssm-cloner comes for your help.

* Just execute this module and pass on the parameters and it will clone the documents for you.

* You can also use it to unclone or create new version for your documents.


## Pre-requisites
---
* AWS CLI should be installed on the system. For installing AWS CLI, visit the link: [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

* Python should be installed. For installing Python, visit this link: [Installing Python](https://realpython.com/installing-python/)

* Python package boto3 should be installed.
  ```Bash
  pip3 install boto3 #(Linux)
  or
  pip install boto3 #(Windows)
  ```

## Execution Types
---
1. Execute from command line as command line program

2. Use it as a module - PENDING

3. Use it as a installer - PENDING

## Execution Steps
---
1. Clone the repo in your system

2. Go to the directory where the repo is cloned

3. Open the terminal in the directory and run the below commands.

4. Execute the program using below syntax (For Linux):
   ```Bash
    #For Cloning (Linux)
    python3 ssm_cloner.py -c -d <doc_name> -sr <source_region> -dr <command_separated_destination_regions>

    #For Uncloning (Linux)
    python3 ssm_cloner.py -uc -d <doc_name> -sr <source_region> -dr <command_separated_destination_regions>
   ```

5. For windows, follow the below syntax:
   ```powershell

    #For Cloning (Windows)
    python ssm_cloner.py -c -d <doc_name> -sr <source_region> -dr <command_separated_destination_regions>

    #For Uncloning (Windows)
    python ssm_cloner.py -uc -d <doc_name> -sr <source_region> -dr <command_separated_destination_regions>
   ```


## Command Line Parameters Description
---
1. ***-d / --doc-name*** (Required): This parameter is used to define the document name that needs to be cloned.

2. ***-sr / --source-region*** (Required): This parameter is used to define the source region from which the main document will be fetched

    * Type: string
    * Example: us-east-1
######
1. ***-dr / --destination-regions*** (Required): This parameter is used to define the destination regions to which the cloned documents will be created.

   * Type: Command Separated values
   * Example: us-east-1,us-east-2,us-west-1

######
1. ***-c / --clone*** (Required): This parameter is used to specify program to clone the document. This parameter cannot be used together with "-uc / --unclone" parameter.

   * Type: None
   * Example: -c or --clone
   * Usage:
     ```bash
     python3 ssm_cloner.py -c #(Short hand parameter)

     # OR

     python3 ssm_cloner.py --clone #(Descriptive parameter)
     ```

######
5. ***-uc / --unclone*** (Required): This parameter is used to specify program to unclone the document. This parameter cannot be used together with "-c or --clone" parameter.

   * Type: None
   * Example: -uc or --unclone
   * Usage:
     ```bash
     python3 ssm_cloner.py -uc #(Short hand parameter)

     #OR

     python3 ssm_cloner.py --unclone #(Descriptive parameter)
     ```


## Roadmap
---
* Add the functionality to make the program, a module
* Add the functionality to execute the program across the accounts/region
* Support for gov cloud

## Links
---
* pypi - https://pypi.org/project/ssm-cloner/
* Github - https://github.com/lovepurohit/ssm-cloner
