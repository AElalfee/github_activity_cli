import json
import urllib.error as err
import urllib.request as req


def get_activities(username: str):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with req.urlopen(url) as response:
            if response.status == 200:
                events = json.loads(response.read().decode("utf-8"))
                print("Output:")
                for event in events:
                    if event["type"] == "PushEvent":
                        print(
                            f"User {username} pushed to {event['repo']['name']} at {event['created_at']}"
                        )
                    if event["type"] == "PullRequestEvent":
                        print(
                            f"User {username} created a pull request in {event['repo']['name']} at {event['created_at']}"
                        )
                    if event["type"] == "IssueCommentEvent":
                        print(
                            f"User {username} commented on an issue in {event['repo']['name']} at {event['created_at']}"
                        )
                    if event["type"] == "IssuesEvent":
                        print(
                            f"User {username} created issue in {event['repo']['name']} at {event['created_at']}"
                        )
                    if event["type"] == "WatchEvent":
                        print(
                            f"User {username} starred {event['repo']['name']} at {event['created_at']}"
                        )
                    if event["type"] == "CreateEvent":
                        print(
                            f"User {username} created a new repository {event['repo']['name']} at {event['created_at']}"
                        )
                    if event["type"] == "PullRequestReviewEvent":
                        print(
                            f"User {username} reviewed a pull request in {event['repo']['name']} at {event['created_at']}"
                        )
            else:
                print(f"Error: HTTP {response.status}")
    except err.URLError as e:
        print(f"Failed to fetch data: {e.reason}")
    except json.JSONDecodeError:
        print("Failed to parse JSON.")
