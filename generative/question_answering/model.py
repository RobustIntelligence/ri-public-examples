"""Model implementation using a fake model."""
from typing import Optional


def generate(
    system_prompt: str,
    prompt: Optional[str],  # noqa: ARG001 (unused-function-argument)
) -> str:
    """Generate a fake response."""
    return system_prompt
