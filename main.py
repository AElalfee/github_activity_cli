import argparse

from requests import get_activities


def main():
    parser = argparse.ArgumentParser(
        prog="GACLI",
        description="A simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal.",
        usage="%(prog)s [options]",
        epilog="For more information, visit https://github.com/AElalfee/github_activity_cli",
    )

    parser.add_argument("username", help="Username to fetch for it's activity.")

    args = parser.parse_args()

    get_activities(args.username)


if __name__ == "__main__":
    main()
