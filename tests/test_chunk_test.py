import pytest  # pytest test framework
from SeqKitSTP.modules import chunk_text  # module under test


# ------------------------------
# Tests for chunk_string()
# ------------------------------

def test_chunk_string_regular_case():
    # Typical DNA sequence input.
    seq = "aggagtaagcccttgcaactggaaatacacccattg"

    # Expect fixed-width chunks of 5 bases.
    # Final chunk may be shorter if sequence length is not divisible by 5.
    expected = [
        'aggag', 'taagc', 'ccttg', 'caact',
        'ggaaa', 'tacac', 'ccatt', 'g'
    ]

    # Verify normal chunking behaviour.
    assert chunk_text.chunk_string(seq, 5) == expected


def test_chunk_string_chunk_size_as_string():
    # chunk_by must be an integer.
    seq = "aggagtaagcccttgcaactggaaatacacccattg"

    # A string should fail because slicing expects an integer index.
    with pytest.raises(TypeError):
        chunk_text.chunk_string(seq, "5")


def test_chunk_string_empty_sequence():
    # Empty input should return an empty list rather than fail.
    assert chunk_text.chunk_string("", 5) == []


def test_chunk_string_chunk_larger_than_sequence():
    # If chunk size exceeds sequence length,
    # the whole sequence should be returned as one chunk.
    assert chunk_text.chunk_string("agg", 10) == ["agg"]


# ------------------------------
# Tests for chunk_string_to_blocks()
# ------------------------------

def test_chunk_string_to_blocks_regular_input():
    # 20 bases total.
    seq = "ACTGGTAGTCAGTCAAGTCA"

    # Chunk into blocks of 5 bases,
    # with 2 blocks per printed row.
    result = chunk_text.chunk_string_to_blocks(seq, 5, 2)

    # Lowercase conversion is enabled by default.
    assert result == [
        ['actgg', 'tagtc'],
        ['agtca', 'agtca']
    ]


def test_chunk_string_to_blocks_partial_final_row():
    # 12 bases total.
    seq = "AAAGGGCCCTTT"

    # 4-base chunks -> 3 chunks total.
    # 2 blocks per row means final row will be incomplete.
    result = chunk_text.chunk_string_to_blocks(seq, 4, 2)

    assert result == [
        ['aaag', 'ggcc'],
        ['cttt']
    ]


def test_chunk_string_to_blocks_exact_fit():
    # 12 bases.
    seq = "AAAAGGGGCCCC"

    # 4-base chunks, 3 blocks per row -> exact single-row fit.
    result = chunk_text.chunk_string_to_blocks(seq, 4, 3)

    assert result == [
        ['aaaa', 'gggg', 'cccc']
    ]


def test_chunk_string_to_blocks_multi_line_input():
    # Input copied from wrapped text or pasted sequence file.
    # Includes spaces and newlines.
    seq = """AAAAGGGG
             CCCC TTTT
             GGGGAAAA"""

    # Internal whitespace should be stripped before chunking.
    result = chunk_text.chunk_string_to_blocks(seq, 4, 2)

    assert result == [
        ['aaaa', 'gggg'],
        ['cccc', 'tttt'],
        ['gggg', 'aaaa']
    ]


def test_chunk_string_to_blocks_disable_lowercase():
    # Mixed-case sequence.
    seq = "AaAaGGgg"

    # Explicitly preserve original case.
    result = chunk_text.chunk_string_to_blocks(
        seq,
        2,
        2,
        return_lowercase=False
    )

    assert result == [
        ['Aa', 'Aa'],
        ['GG', 'gg']
    ]


def test_chunk_string_to_blocks_empty_input():
    # Empty input should safely return an empty structure.
    assert chunk_text.chunk_string_to_blocks("", 4, 3) == []


def test_chunk_string_to_blocks_chunk_as_string_raises():
    # chunk_by must be integer.
    with pytest.raises(TypeError):
        chunk_text.chunk_string_to_blocks("AAGGTT", "2", 2)


def test_chunk_string_to_blocks_num_blocks_as_string_raises():
    # num_blocks must be integer.
    with pytest.raises(TypeError):
        chunk_text.chunk_string_to_blocks("AAGGTT", 2, "2")


def test_chunk_string_to_blocks_invalid_chunk_type_raises():
    # Same validation as above, using a different numeric argument combination.
    with pytest.raises(TypeError):
        chunk_text.chunk_string_to_blocks("AAGGTT", "2", 3)


def test_chunk_string_to_blocks_invalid_num_blocks_type_raises():
    # Same validation as above, using a different numeric argument combination.
    with pytest.raises(TypeError):
        chunk_text.chunk_string_to_blocks("AAGGTT", 3, "3")

