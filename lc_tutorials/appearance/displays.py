"""This module contains functions for displaying anything from tool results to i/o."""
from IPython.display import display, HTML
import uuid


def display_tavily_search_results(results: list[dict[str, str]]) -> None:
    """Displays the tavilty search results in a visually formatted HTML structure within our notebook.

    This function takes a list of search results, formats each result into a styled HTML
    "card," and displays it in a Jupyter notebook. Each card includes the URL as a clickable
    link and a content snippet. We added the CSS for this rendering in the first cell of the NB.

    Args:
        results (list[dict[str, str]]):
            A list of dictionaries containing 'url' and 'content' keys, where:
                - 'url' (str): The link to the search result.
                - 'content' (str): A short snippet or description of the result.

    Returns:
        None; The function outputs HTML directly in our notebook and does not return any value.
    """

    # Generate a unique prefix to ensure unique IDs
    unique_prefix = str(uuid.uuid4()).replace("-", "")

    # Begin constructing the HTML content
    html_content = "<div class='result-container'>"

    # Iterate through the results
    for idx, result in enumerate(results):
        # Each result gets a unique ID for the collapsible functionality
        content_id = f"result-content-{unique_prefix}-{idx}"
        icon_id = f"icon-{unique_prefix}-{idx}"
        html_content += f"""
        <div class="result-card">
            <div class="result-header" onclick="toggleContent('{content_id}', '{icon_id}')">
                <span>URL:</span> <a href="{result['url']}" target="_blank" class="result-link">{result['url']}</a>
                <span id="{icon_id}" style="float: right;">&#9654;</span>  <!-- Right-facing arrow initially -->
            </div>
            <div id="{content_id}" class="result-content">
                <p style="font-family: Montserrat"><strong>CONTENT:</strong><br><br> {result['content']}</p>
            </div>
        </div>
        """
    html_content += "</div>"

    # Display the final HTML with CSS and JavaScript
    display(HTML(html_content))