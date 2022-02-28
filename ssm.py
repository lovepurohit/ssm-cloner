"""Module for Base SSM utilities class."""
import boto3


class Ssm:
    """Main class for SSM."""

    def __init__(self, *, doc_name, source_region, destination_region, action_type) -> None:
        """Initialize all the necessary variable.

        Args:
            doc_name (string): SM document name which you want to use
            source_region (string): Source region from which you want to get the main document details
            destination_region (string): Destination region at which you want to perform the action
            action_type (string): Action type used to determine the client. Values: clone || unclone

        Return: None
        """
        self.source_client = boto3.client('ssm', region_name=source_region)
        self.destination_client = boto3.client(
            'ssm', region_name=destination_region)
        self.doc_name = doc_name
        self.doc_name_copy = doc_name + "_cloned" + f"_{destination_region}"
        self.action_type = action_type
        if action_type == 'clone':
            if self.is_doc_exists(doc_name=self.doc_name):
                self.doc_content = self.get_doc_contents()
            else:
                # print("Source Document does not exists")
                raise Exception("Source Document does not exists.")

    def create_document(self, *, doc_name=None, contents=None, doc_type='Command', doc_format='JSON', targe_type='/'):
        """Create SSM document.

        Args:
            None
        Return:
            Successfull: True
            Unsuccessfull: False
        """
        doc_name = doc_name if doc_name is not None else self.doc_name_copy
        contents = contents if contents is not None else self.doc_content
        try:
            if not self.is_doc_exists(doc_name=doc_name, dest_client=True):
                response = self.destination_client.create_document(
                    Content=contents,
                    Name=doc_name,
                    DocumentType=doc_type,
                    DocumentFormat=doc_format,
                    TargetType=targe_type
                )
                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    print("Successfully cloned the document: {}".format(doc_name))
                else:
                    print("Unsuccessfull to clone SM document: {}".format(doc_name))
            else:
                print("Document already exists in the account/region")

        except Exception as error:
            print(error)
            print("Failed to cloned document in the customer account/region")
            raise error from Exception

    def delete_document(self, *, doc_name=None):
        """Delete SSM document.

        Args:
            docName: SSM Document Name

        Return:
            Successfull: True
            Unsuccessfull: False
        """
        try:
            doc_name = doc_name if doc_name is not None else self.doc_name_copy
            if self.is_doc_exists(doc_name=doc_name):

                response = self.destination_client.delete_document(
                    Name=doc_name
                )
                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    print("Successfully uncloned the document: {} from the account/region".format(
                        doc_name))
                else:
                    print("Unsuccessfull to unclone the document: {} from the account/region".format(
                        doc_name))
            else:
                print(f"Document does not exists: {doc_name}")

        except Exception as error:
            print(error)
            print("Failed to unclone the document from the account/region.")
            raise error from Exception

    def is_doc_exists(self, *, doc_name, dest_client=False):
        """Fetch full name of the SSM document, i.e., ARN of the document.

        Args: None

        Return:
            Successfull: True
            Unsuccessfull: False
        """
        try:
            doc_name = doc_name if doc_name is not None else self.doc_name_copy
            if self.action_type == 'clone' and not dest_client:
                client = self.source_client
            else:
                client = self.destination_client
            paginator = client.get_paginator('list_documents')
            responseIterator = paginator.paginate(
                DocumentFilterList=[
                    {
                        'key': 'Owner',
                        'value': 'Self'
                    }
                ]
            )

            responseList = []
            for response in responseIterator:
                responseList.extend(response['DocumentIdentifiers'])

            documents = responseList
            exist = False
            for document in documents:
                if doc_name in document['Name']:
                    exist = True

            return exist
        except Exception as error:
            print(error)

    def get_doc_contents(self, *, doc_name=None):
        """Fetch contents the SSM document.

        Args: None

        Return:
            Successfull: SSM document contents
            Unsuccessfull: False
        """
        try:
            doc_name = doc_name if doc_name is not None else self.doc_name_copy
            if self.action_type == 'clone':
                client = self.source_client
            else:
                client = self.destination_client
            response = client.get_document(
                Name=self.doc_name,
                DocumentFormat='JSON'
            )
            return response['Content']
        except Exception as error:
            print(error)
            print(
                "Failed to get the contents of the SSM document from source/destination region")
            raise error from Exception
