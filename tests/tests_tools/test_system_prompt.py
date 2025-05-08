"""Tests for `azrock.system_prompt`."""

from azrock.system_prompt import AZROCK_SYSTEM_PROMPT_TEMPLATE
from jinja2 import Template


def test_azrock_system_prompt():
    assert isinstance(AZROCK_SYSTEM_PROMPT_TEMPLATE, str)


def test_validate_system_prompt():
    # Create a template object from the system prompt
    template = Template(AZROCK_SYSTEM_PROMPT_TEMPLATE)

    # Sample data that matches the template's expected structure
    sample_data = {
        "tools": {
            "tool1": {
                "name": "test_tool",
                "inputs": {
                    "arg1": {"type": "str", "description": "Test argument 1"},
                    "arg2": {"type": "int", "description": "Test argument 2"},
                },
                "output_type": "str",
                "description": "A test tool",
            }
        },
        "managed_agents": {
            "agent1": {"name": "test_agent", "description": "A test agent"}
        },
        "authorized_imports": ["os", "sys"],
    }

    # Attempt to render the template with sample data
    # This will raise an exception if there are any Jinja syntax errors
    rendered = template.render(**sample_data)

    # Basic validation that the template rendered something
    assert isinstance(rendered, str)
    assert len(rendered) > 0
