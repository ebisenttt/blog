import subprocess
from subprocess import PIPE
import bs4
import re
import tweepy
import os
from dotenv import load_dotenv

def main():
	new_article_arr = get_new_article_path_list()
	if not len(new_article_arr):
		print("Complite: No new article is detected")
		return
	for path in new_article_arr:
		title = get_article_title(path)
		print("New article title is", title)
		api = make_api()
		tweet_text = "新しい記事を投稿しました:\n" + title + "\n"
		result = api.create_tweet(text=text)
		print(result)
	return

def convert_title(string):
	string = re.sub('\n', '', string)
	string = re.sub('\s', '', string)
	string = string.replace("&vert", "|")
	return string

def get_new_article_path_list():
	COMMAND = "git diff --name-only --cached --diff-filter=A"
	process = subprocess.run(COMMAND, shell=True, stdout=PIPE, stderr=PIPE, text=True)
	path_text = process.stdout
	path_arr = path_text.split("\n")[:-1]
	path_arr_of_new_article = list(
		filter(
			lambda path: path.startswith("docs/article"),
			path_arr
		))
	return path_arr_of_new_article

def get_article_title(path):
	soup = bs4.BeautifulSoup(open(path), "html.parser")
	title = convert_title(soup.title.string)
	return title

def make_api():
	API_KEY = os.environ["TWITTER_API_KEY"]
	API_KEY_SECRET = os.environ["TWITTER_API_KEY_SECRET"]
	ACCESS_TOKEN = os.environ["TWITTER_API_ACCESS_TOKEN"]
	ACCESS_TOKEN_SECRET = os.environ["TWITTER_API_ACCESS_TOKEN_SECRET"]

	client = tweepy.Client(
		consumer_key=API_KEY,
		consumer_secret=API_KEY_SECRET,
		access_token=ACCESS_TOKEN,
		access_token_secret=ACCESS_TOKEN_SECRET
	)
	return client

if __name__ == "__main__":
	load_dotenv()
	main()