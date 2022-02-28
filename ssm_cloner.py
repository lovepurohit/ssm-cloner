"""Main module for the project."""
from clone_doc import clone_ssm_doc
from unclone_doc import unclone_ssm_doc
from parse_arguments import parse_arguments


def clone(*, doc_name, source_region, destination_regions):
    """Clone the SSM document.
    Args:
        doc_name (string): Base document name that you want to unclone
        source_region (string): Source region from which you want to get the main document details
        destination_regions (list): List of regions at which you want to clone the document

    Returns: None
    """
    if not isinstance(doc_name, str):
        raise TypeError(
            f"Type of doc_name is not correct. Found type: {type(doc_name)}. Valid type: {type('')}")
    if not isinstance(source_region, str):
        raise TypeError(
            f"Type of source_region is not correct. Found type: {type(source_region)}. Valid type: {type('')}")
    if not isinstance(destination_regions, list):
        raise TypeError(
            f"Type of destination_regions is not correct. Found type: {type(destination_regions)}. Valid type: {type([])}")
    # Perform the action based on the clone event
    print(
        f"Cloning the document: {doc_name} from source region: {source_region} to destination regions: {destination_regions}")
    print('-'*80)
    res = clone_ssm_doc(doc_name=doc_name, source_region=source_region,
                        destination_regions=destination_regions)
    print(f"Clone Result: {res}")
    print('-'*80)
    return res


def unclone(*, doc_name, source_region, destination_regions):
    """Unclone the SSM document.

    Args:
        doc_name (string): Base document name that you want to unclone
        source_region (string): Source region from which you want to get the main document details
        destination_regions (list): List of regions from which you want to unclone the document

    Returns: None
    """
    if not isinstance(doc_name, str):
        raise TypeError(
            f"Type of doc_name is not correct. Found type: {type(doc_name)}. Valid type: {type('')}")
    if not isinstance(source_region, str):
        raise TypeError(
            f"Type of source_region is not correct. Found type: {type(source_region)}. Valid type: {type('')}")
    if not isinstance(destination_regions, list):
        raise TypeError(
            f"Type of destination_regions is not correct. Found type: {type(destination_regions)}. Valid type: {type([])}")
    # Perform the action based on the unclone event
    print(
        f"Uncloning the document: {doc_name} from source region: {source_region} to destination regions: {destination_regions}")
    print('-'*80)
    res = unclone_ssm_doc(doc_name=doc_name, source_region=source_region,
                          destination_regions=destination_regions)
    print(f"Unclone Result: {res}")
    print('-'*80)
    return res


def main(event, context):
    """Main function.

    Args:
        event (JSON): Event is only used if anyone wants to use it in lambda function. Otherwise ignore it.
        context (JSON): Context is only used if anyone wants to use it in lambda function. Otherwise ignore it.

    Returns: None
    """
    # Getting the arguments from command line
    args = parse_arguments()

    # Convert the regions into list
    destination_regions = [item.strip()
                           for item in args.destination_regions.split(',')]

    # Getting the other arguments and storing it in variables
    source_region = args.source_region
    doc_name = args.main_doc_name
    res = {}

    # Check for various args and act acc to it.
    if args.clone:
        res = clone(doc_name=doc_name, source_region=source_region,
                    destination_regions=destination_regions)

    if args.unclone:
        res = unclone(doc_name=doc_name, source_region=source_region,
                      destination_regions=destination_regions)

    return res


if __name__ == '__main__':
    # Calling the main function
    main(event=None, context=None)
