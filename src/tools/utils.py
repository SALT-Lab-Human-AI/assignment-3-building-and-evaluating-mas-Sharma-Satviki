# src/tools/utils.py

def truncate_text(text: str, max_chars: int = 400) -> str:
    """Return text truncated to max_chars, with ellipsis."""
    if not isinstance(text, str):
        return ""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."
