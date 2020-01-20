from bs4 import BeautifulSoup
import requests

# def findAuthor():
# 	with open('poem_of_the_day.html') as html_file:
# 		soup = BeautifulSoup(html_file, 'lxml')
# 	return soup.find("div", {"class": "daily_poem_author"}).text

# def findPoemText():
# 	with open('poem_of_the_day.html') as html_file:
# 		soup = BeautifulSoup(html_file, 'lxml')
# 	poemHtml = soup.find_all("span", {"class": "excerpt_line"})
# 	poemLines = []
# 	for pline in poemHtml:
# 		#print(pline.text)
# 		poemLines.append(pline.text)
# 	return poemLines

def completePoem():
	with open('./myhomepage/poem_of_the_day.html') as html_file:
		soup = BeautifulSoup(html_file, 'lxml')

	author = soup.find("div", class_="daily_poem_author").text.strip()
	
	poemHtml = soup.find_all("span", {"class": "excerpt_line"})
	poemLines = []
	for pline in poemHtml:
		#print(pline.text)
		poemLines.append(pline.text)

	return {'poemAuthor':author, 'poemBody':poemLines}

# myarticle = soup.find_all("div", {"class": "elementor-shortcode"})

# print(myarticle[1].parent.parent)

# author = findAuthor(soup).strip()
# poemBody = findPoemText(soup)

# print("Author: " + author)

# for line in poemBody:
#	print(line)