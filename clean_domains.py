import os
import sys
import random


def main(fileName, domainList):
	mailData = []

	listPath = os.getcwd() + "/" + fileName
	with open(listPath, "r") as listIn:
		for email in listIn: # email list iterate over it
			badDomain = False

			for domainName in domainList:
				if domainName in email.lower():
					badDomain = True

			if badDomain == False:
				mailData.append(email.rstrip().lower())


	newList = []
	for email in mailData:
		if email not in newList:
			newList.append(email)

	random.shuffle(newList)
	print(str(len(newList)) + " Unique emails extracted.")

	with open(os.getcwd() + "/domains_cleaned.log", "a") as fileOut:
		for email in newList:
			fileOut.write(email + "\n")



if __name__ == "__main__":
	try:
		fileName = sys.argv[1]
		domainList = sys.argv[2].split(",")
		main(fileName, domainList)
	except:
		print("Usage: python3 clean_domains.py filename.log domain.com")