import logging  # Standard Python logging support.

# Module-level logger.
# Using __name__ makes log messages traceable to this file.
logger = logging.getLogger(__name__)


def create_genbank_style(chunk_list):
    """
    Convert chunked sequence rows into GenBank-style printable text.

    Parameters:
    chunk_list (list):
        Nested list where each item is one printed row and each row
        contains sequence blocks.

        Example:
        [
            ["atgcttagct", "agcttacgta", "gctagctagc"],
            ["ttagctagct", "agctag"]
        ]

    Returns:
    str:
        Multi-line string formatted in a GenBank-like layout.
    """

    # Tracks the 1-based coordinate printed at the start of each line.
    # In GenBank this is the position of the first base on that row.
    counter = 0

    # Accumulates the final formatted text.
    text_out = ""

    try:
        # Iterate over each row of chunked sequence blocks.
        for line in chunk_list:

            # Move to the first base position of this line.
            #
            # First row:
            # counter = 0 -> 1
            #
            # Later rows:
            # previous loop updates the counter to total bases seen,
            # so adding 1 gives the next 1-based start coordinate.
            counter += 1

            # Join the sequence blocks with spaces.
            #
            # Example:
            # ["atgcttagct", "agcttacgta", "gctagctagc"]
            #
            # becomes:
            # "atgcttagct agcttacgta gctagctagc"
            row = " ".join(line)

            # Append one formatted output line.
            #
            # Example:
            # "1\tatgcttagct agcttacgta gctagctagc\n"
            #
            # \t inserts the gap between coordinate and sequence.
            text_out += "{}\t{}{}".format(str(counter), row, "\n")

            # Update counter to the final base position printed
            # on the current line.
            #
            # row.split() removes spaces between sequence blocks.
            # "".join(...) reconstructs the continuous sequence.
            #
            # Example:
            # "atgcttagct agcttacgta"
            # -> "atgcttagctagcttacgta"
            #
            # len(...) gives number of bases in this line.
            #
            # We subtract 1 because we already added 1 earlier when
            # moving to the start coordinate of this row.
            counter += len("".join(row.split())) - 1

    except TypeError as e:
        # Usually triggered if chunk_list is not iterable or
        # contains non-string values that cannot be joined.
        logger.error(f"create_genbank_style failed with error: {e}")

    # Return the complete GenBank-style text block.
    return text_out

