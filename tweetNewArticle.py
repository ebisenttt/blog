import subprocess
from subprocess import PIPE
import bs4

def main():
	command = "git diff --name-only --cached --diff-filter=A"
	process = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
	pathText = process.stdout
	pathArr = pathText.split("\n")[:-1]
	pathArrOfNewArticle = list(
		filter(
			lambda path: path.startswith("article"),
			pathArr
		))
	print("New file list: ", pathArrOfNewArticle)
	if not len(pathArrOfNewArticle):
		return "Complite: No new article is detected"
	for path in pathArrOfNewArticle:
		soup = bs4.BeautifulSoup(open(path), "html.parser")
		title = soup.title.string
		print("New article title is ", title)


main()