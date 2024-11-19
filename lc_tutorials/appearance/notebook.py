from IPython.display import display, HTML


def apply_custom_styles(use_base: bool = True, custom_style: str = '') -> None:
    """Applies custom CSS styles within Jupyter notebook cell.

    Args:
        use_base (bool): Whether to use the base styles defined in the function.
                         If False, only `custom_style` will be applied. Default is True.
        custom_style (str): Additional CSS styles to apply. If `use_base` is False, this
                            will be the only style applied. If `use_base` is True, it
                            will be appended to the base styles.

    Returns:
        None
    """

    # Base CSS styles
    base_styles = '''
    <style>
    /* Font imports */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Source+Code+Pro:ital,wght@0,200..900;1,200..900&display=swap');

    /* Variables */
    :root {
        --primary-color: #05bfa5;
        --primary-light: #FAFAFA;
        --text-color: #2c3e50;
        --code-bg: #f8f8f8;
        --code-fg: #b22222;
        --success-color: #479269;
        --warning-color: #f39c12;
        --danger-color: #e74c3c;
        --border-radius: 8px;
        --spacing-sm: 0.3em;
        --spacing-md: 1em;
        --spacing-lg: 2em;
    }

    /* Container styles */
    .h1-container, .h2-container, .h3-container {
        font-family: 'Montserrat', sans-serif;
        max-width: 95%;
        margin: var(--spacing-lg) auto;
        line-height: 1.6;
        color: var(--text-color);
    }

    /* List styles */
    .feature-list {
        background-color: var(--primary-light);
        padding: var(--spacing-sm) var(--spacing-lg);
        border-radius: var(--border-radius);
        border-left: 4px solid var(--primary-color);
        margin: var(--spacing-md) 0;
    }

    /* Code styles */
    .code-mention {
        font-family: 'Source Code Pro', monospace !important;
        background-color: var(--code-bg) !important;
        padding: 2px 5px;
        font-weight: 600 !important;
        border-radius: 4px;
        color: var(--code-fg) !important;
    }

    .code-block {
        background-color: var(--primary-light);
        border-left: 4px solid var(--primary-color);
        padding: var(--spacing-md);
        margin: var(--spacing-md) 0;
        border-radius: var(--border-radius);
        padding: var(--spacing-lg);
        max-width: 90%;
    }

    /* Information blocks */
    .note-block, .notice-block {
        padding: var(--spacing-md);
        border-radius: var(--border-radius);
        margin: var(--spacing-md) 0;
    }

    .note-block {
        background-color: var(--primary-light);
        border-left: 4px solid var(--success-color);
    }

    .notice-block {
        background-color: var(--primary-light);
        border-left: 4px solid var(--warning-color);
    }

    .note-title {
        margin-top: 0;
        color: var(--success-color);
        font-weight: 600;
    }

    .feature-list:hover {
        background-color: #f0f0f0;
    }
    .code-block:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Utility styles */
    .code-comment {
        color: #607d8b;
        font-style: italic;
    }

    .highlight {
        background-color: #fff176;
        padding: 2px 5px;
        border-radius: 3px;
    }
    </style>
    '''

    # Remove <style> tags if present
    if custom_style.startswith('<style>'):
        custom_style = custom_style.replace('<style>', '').replace('</style>', '')

    # Combine base styles with custom styles if requested
    final_styles = base_styles if use_base else ''
    final_styles += f"<style>{custom_style}</style>" if custom_style else ''

    # Inject the CSS into the notebook
    display(HTML(final_styles))


# Standard library imports
from IPython.display import Image, display

# Third-party imports
from colorama import Back, Fore, Style


def get_color(color: str | None = None, is_background: bool = False) -> str:
    """Fetches the foreground or background color from colorama dynamically based on the color name.

    Args:
        color (str | None):
            The name of the color.
            Options are:
                - "red", "green", "yellow", "blue", "magenta", "cyan", "white".
        is_background (bool):
            If True, fetches the background color (from `Back`).
            If False, fetches the foreground color (from `Fore`).

    Returns:
        str: The ANSI escape sequence for the requested color.

    Raises:
        ValueError: If an invalid color name is provided.
    """
    if not color:
        return ""

    # Select the colorama module (Fore for foreground, Back for background)
    colorama_module = Back if is_background else Fore
    color_attr = color.upper()  # Convert color name to uppercase to match colorama attributes

    try:
        # Dynamically retrieve the color attribute from Fore or Back
        return getattr(colorama_module, color_attr)
    except AttributeError:
        raise ValueError(f"Invalid color '{color}'. Valid options are: red, green, yellow, blue, magenta, cyan, white.")


def cprint(
        text: str,
        fg_color: str | None = None,
        bg_color: str | None = None,
        bold: bool = False,
        dim: bool = False,
        underline: bool = False,
        prefix_text: str = "",
        bold_prefix: bool = False,
        dim_prefix: bool = False,
        underline_prefix: bool = False,
        return_formatted_text: bool = False
) -> str | None:
    """Formats and prints text with specified foreground and background colors, weight, and additional styling.

    Args:
        text (str):
            The main text to be formatted.
        fg_color (str, optional):
            The name of the Foreground color.
            Options are:
                - "red", "green", "yellow", "blue", "magenta", "cyan", "white".
        bg_color (str, optional):
            The name of the Background color. Same options as FG.
        bold (bool):
            If True, makes the main text bold.
        dim (bool):
            If True, dims the main text.
        underline (bool):
            If True, underlines the main text.
        prefix_text (str):
            Optional prefix text to be formatted and displayed before the main text.
        bold_prefix (bool):
            If True, makes the prefix text bold.
        dim_prefix (bool):
            If True, dims the prefix text.
        underline_prefix (bool):
            If True, underlines the prefix text.
        return_formatted_text (bool):
            If True, returns the formatted text as a string instead of printing it.

    Returns:
        str | None: Formatted text string if `return_formatted_text` is True, otherwise None.

    Raises:
        ValueError: If an invalid foreground or background color is provided.
    """

    # Helper function to build formatted text based on parameters
    def format_text(text: str, fg_color: str | None, bg_color: str | None, bold: bool, dim: bool,
                    underline: bool) -> str:
        """Helper function to format text using Colorama styling."""
        formatted = ""
        if fg_color:
            formatted += get_color(fg_color)
        if bg_color:
            formatted += get_color(bg_color, is_background=True)
        if bold:
            formatted += Style.BRIGHT
        elif dim:
            formatted += Style.DIM
        if underline:
            formatted += "\033[4m"  # ANSI code for underline
        return formatted + text + Style.RESET_ALL

    # Format the prefix text with default main text styling, modified by any prefix-specific flags
    formatted_prefix = ""
    if prefix_text:
        # Apply the same fg_color and bg_color as the main text, and apply bold, dim, underline only if specified for the prefix
        formatted_prefix = format_text(
            prefix_text,
            fg_color=fg_color,
            bg_color=bg_color,
            bold=bold_prefix if bold_prefix else bold,
            dim=dim_prefix if dim_prefix else dim,
            underline=underline_prefix if underline_prefix else underline
        )

    # Format the main text with specified styling
    formatted_text = format_text(
        text,
        fg_color=fg_color,
        bg_color=bg_color,
        bold=bold,
        dim=dim,
        underline=underline
    )

    # Combine prefix and main text
    final_output = formatted_prefix + formatted_text

    # Return or print the final output based on `return_formatted_text`
    if return_formatted_text:
        return final_output
    print(final_output)


