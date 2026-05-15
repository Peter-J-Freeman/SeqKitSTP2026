import logging  # Import Python's standard logging module.

# Create a module-level logger.
# __name__ makes the logger inherit the module's name,
# which helps identify where messages come from.
logger = logging.getLogger(__name__)


def chunk_string(query_sequence, chunk_by):
    """
    Split a DNA sequence into evenly sized chunks.

    Parameters:
    query_sequence (str): The DNA sequence string to be split.
    chunk_by (int): The length of each chunk.

    Returns:
    list: A list of fixed-length chunks.
    """

    # Record that chunking has started.
    logger.info("Chunking sequence into blocks of {}".format(chunk_by))

    # Container for sequence chunks.
    my_list = []

    try:
        # Continue until the full sequence has been consumed.
        while query_sequence:

            # Take the first `chunk_by` bases and store them.
            # Example: "acgtacgt", chunk_by=4 -> "acgt"
            my_list.append(query_sequence[:chunk_by])

            # Remove the chunk we just stored.
            # Remaining sequence becomes the next iteration input.
            query_sequence = query_sequence[chunk_by:]

    except TypeError as e:
        # Usually triggered if query_sequence is not string-like
        # or chunk_by is not usable as a slice boundary.
        logger.error("Chunking failed with exception: {}".format(e))
        raise

    # Return flat list of chunks.
    # Example: ["acgt", "acgt", "ttaa"]
    return my_list


def chunk_string_to_blocks(query_sequence, chunk_by, num_blocks, return_lowercase=True):
    """
    Formats a DNA sequence into a list of chunked sequences:
    Each line contains `num_blocks` blocks of length `chunk_by`,
    with a counter at the start.

    This is useful for GenBank-style formatting, where sequence
    is printed in grouped blocks across multiple rows.

    Parameters:
    query_sequence (str): The DNA sequence to be formatted.
    chunk_by (int): The length of each chunk/block.
    num_blocks (int): Number of blocks per line.
    return_lowercase (bool): If True, converts sequence to lowercase
                             (GenBank convention).

    Returns:
    list: A list of rows, where each row is a list of blocks.
    """

    # Log the intended formatting structure.
    logger.info(
        "Chunking sequence into rows of {} blocks of {}".format(
            num_blocks, chunk_by
        )
    )

    # Defensive validation:
    # slicing and range() both expect integers here.
    if not isinstance(chunk_by, int) or not isinstance(num_blocks, int):
        raise TypeError(
            f"chunk_by {chunk_by} and num_blocks {num_blocks} must be integers."
        )

    try:
        # Remove all whitespace first.
        # This allows input sequences copied from FASTA, GenBank,
        # wrapped text, or pasted multi-line sequence blocks.
        #
        # Example:
        # "ACGT ACGT\nTTAA"
        # becomes:
        # "ACGTACGTTTAA"
        query_sequence = "".join(query_sequence.split())

        # GenBank sequence sections are conventionally lowercase.
        # FASTA sequence bodies are often uppercase.
        if return_lowercase:
            query_sequence = query_sequence.lower()

        # Step 1:
        # Split the sequence into fixed-length chunks.
        #
        # Example:
        # "acgtacgtttaa", chunk_by=4
        # -> ["acgt", "acgt", "ttaa"]
        flat_chunks = chunk_string(query_sequence, chunk_by)

        # Step 2:
        # Group the chunks into rows of `num_blocks`.
        #
        # Example:
        # flat_chunks = ["aaa", "bbb", "ccc", "ddd"]
        # num_blocks = 3
        #
        # Result:
        # [["aaa", "bbb", "ccc"], ["ddd"]]
        full_list = [
            flat_chunks[i:i + num_blocks]
            for i in range(0, len(flat_chunks), num_blocks)
        ]

    except TypeError as e:
        # Re-log failure with context.
        logger.error("Chunking to blocks failed with exception: {}".format(e))
        raise

    # Return nested list ready for pretty-printing.
    return full_list
