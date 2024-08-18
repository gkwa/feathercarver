from feathercarver import fix_markdown_links


def test_fix_markdown_links():
    input_content = """
   [Link 1
   ](https://example.com)

   Normal text

   ```
   [Code block link
   ](https://example.com)
   ```

   [Link 2
   ](https://another-example.com)
   """

    expected_output = """
   [Link 1](https://example.com)

   Normal text

   ```
   [Code block link
   ](https://example.com)
   ```

   [Link 2](https://another-example.com)
   """

    assert fix_markdown_links(input_content) == expected_output


def test_no_changes_needed():
    input_content = """
   [Normal link](https://example.com)

   ```
   [Code block link
   ](https://example.com)
   ```
   """

    assert fix_markdown_links(input_content) == input_content


def test_multiple_newlines_in_link_text():
    input_content = """
   [

   Link

   with

   newlines

   ](https://example.com)
   """

    expected_output = """
   [Link with newlines](https://example.com)
   """

    assert fix_markdown_links(input_content) == expected_output


def test_multiple_newlines_in_link_text_within_code_block():
    input_content = """
   [ Link with newlines ](https://example.com)

   ```
   [

   Link

   with

   newlines

   ](https://example.com)
   ```
   """

    expected_output = """
   [Link with newlines](https://example.com)

   ```
   [

   Link

   with

   newlines

   ](https://example.com)
   ```
   """

    assert fix_markdown_links(input_content) == expected_output


def test_inline_code_block():
    input_content = """
    This is a paragraph with an inline code block: `a link [ a   ](url) ` and some more text.
    
    Here's another paragraph with a [regular link](https://example.com) for comparison.
    """

    expected_output = """
    This is a paragraph with an inline code block: `a link [ a   ](url) ` and some more text.
    
    Here's another paragraph with a [regular link](https://example.com) for comparison.
    """

    assert fix_markdown_links(input_content) == expected_output


def test_multiple_newlines_in_url():
    input_content = """
   [Link](

   https://example.com

   )
   """

    expected_output = """
   [Link](https://example.com)
   """

    assert fix_markdown_links(input_content) == expected_output


def test_newlines_in_both_link_text_and_url():
    input_content = """
   [

   Complex

   Link

   ](

   https://

   example.com

   )
   """

    expected_output = """
   [Complex Link](https://example.com)
   """

    assert fix_markdown_links(input_content) == expected_output


def test_multiple_links():
    input_content = """
   [Link 1
   ](url1)

   Some text

   [

   Link 2

   ](

   url2

   )

   More text

   [Link 3](url3)
   """

    expected_output = """
   [Link 1](url1)

   Some text

   [Link 2](url2)

   More text

   [Link 3](url3)
   """

    assert fix_markdown_links(input_content) == expected_output
