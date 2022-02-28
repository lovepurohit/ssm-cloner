"""Module for uncloning the SSM document."""
from ssm import Ssm


def unclone_ssm_doc(doc_name, source_region, destination_regions):
    """Unclone method for documents.
    Args:
        doc_name (string): Base document name that you want to unclone
        source_region (string): Source region from which you want to get the main document details
        destination_regions (list): List of regions from which you want to unclone the document

    Returns:
        status (dict): Dict of regions with their status
    """
    status = {}
    print(f"Executing it in source region: {source_region}")
    for destination_region in destination_regions:
        try:
            print(f"Executing it in destination region: {destination_region}")
            ssm_object = Ssm(doc_name=doc_name, source_region=source_region,
                             destination_region=destination_region, action_type='unclone')

            # Unclone the document from another regions
            response_unclone = ssm_object.delete_document()
            status.update({destination_region: True})
            print('-'*40)
        except Exception as error:
            print(error)
            status.update({destination_region: False})
            print('-'*40)

    return status
