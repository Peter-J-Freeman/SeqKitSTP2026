from SeqKitSTP.modules import genbank_style


def test_create_genbank_style_typical():
    # Nested chunk structure produced by chunk_string_to_blocks().
    # Each inner list represents one printed row.
    chunk_list = [
        ['atgc', 'ggta', 'ccta'],  # 4 + 4 + 4 = 12 bases
        ['ttaa', 'ccgg'],          # 4 + 4 = 8 bases
        ['ggcc']                   # 4 bases
    ]

    # Render into GenBank-style printable text.
    result = genbank_style.create_genbank_style(chunk_list)

    # Expected left-hand coordinates:
    #
    # Row 1 starts at base 1
    # Row 2 starts after 12 bases -> 13
    # Row 3 starts after another 8 bases -> 21
    expected = (
        "1\tatgc ggta ccta\n"
        "13\tttaa ccgg\n"
        "21\tggcc\n"
    )

    # Confirm both sequence formatting and coordinate numbering.
    assert result == expected


def test_create_genbank_style_partial_final_row():
    # Final row contains fewer sequence blocks than previous rows.
    chunk_list = [
        ['atgc', 'ggta', 'ccta'],  # 12 bases
        ['ttaa']                   # 4 bases
    ]

    result = genbank_style.create_genbank_style(chunk_list)

    # Second row should begin immediately after base 12.
    expected = (
        "1\tatgc ggta ccta\n"
        "13\tttaa\n"
    )

    assert result == expected


def test_create_genbank_style_empty():
    # Empty chunk input should produce empty output
    # rather than an exception or blank line.
    assert genbank_style.create_genbank_style([]) == ""


def test_create_genbank_style_single_chunk():
    # Simplest valid input:
    # one row containing one sequence block.
    chunk_list = [['atgc']]

    result = genbank_style.create_genbank_style(chunk_list)

    # Single row always starts at coordinate 1.
    expected = "1\tatgc\n"

    assert result == expected


def test_create_genbank_style_invalid_input_logs_error(monkeypatch):
    # Verify that invalid input is handled gracefully
    # and that an error is logged.

    # Dictionary used to capture the logger message.
    called = {}

    def fake_error(msg):
        # Store the logged message for later assertions.
        called['msg'] = msg

    # Replace logger.error with our test stub.
    monkeypatch.setattr(genbank_style.logger, "error", fake_error)

    # Invalid input:
    # None is not iterable, so the function should hit the exception path.
    result = genbank_style.create_genbank_style(None)

    # Current implementation returns empty string on failure.
    assert result == ""

    # Confirm logger.error was called.
    assert 'msg' in called

    # Confirm the expected error wording was emitted.
    assert "failed with error" in called['msg']
