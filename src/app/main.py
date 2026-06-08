from app.bootstrap.cli_actions.app import app
from app.bootstrap.cli_actions import menu, commands  # noqa: F401

def main() -> None:
    app()

if __name__ == "__main__":
    main()