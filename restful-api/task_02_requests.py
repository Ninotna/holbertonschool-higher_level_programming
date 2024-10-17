#!/usr/bin/python3

"""_summary_"""

import csv
import requests


# Function to fetch and print post titles
def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the titles.
    """
    # Fetch posts from JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=10)

    # Print the status code
    print("Status Code:", response.status_code)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data into JSON
        posts = response.json()

        # Print the titles of all posts
        for post in posts:
            print("Title:", post["title"])
    else:
        print("Failed to fetch posts.")


# Function to fetch and save posts to CSV
def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them into a CSV file.
    """
    # Fetch posts from JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data into JSON
        posts = response.json()

        # Prepare data to be saved into CSV
        post_data = []
        for post in posts:
            post_dict = {"id": post["id"], "title": post["title"], "body": post["body"]}
            post_data.append(post_dict)

        # Write the data into posts.csv
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(post_data)
        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts.")


# Call the functions
# fetch_and_print_posts()
# fetch_and_save_posts()
