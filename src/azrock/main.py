"""Main module."""

from smolagents import GradioUI
from azrock.agent import create_agent


def main():
    """Main function."""

    agent = create_agent()
    GradioUI(agent).launch()


if __name__ == "__main__":
    main()
