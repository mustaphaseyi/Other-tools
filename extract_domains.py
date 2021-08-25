import os
import sys
import random


def main(fileName, domainList):
	mailData = []

	listPath = os.getcwd() + "/" + fileName
	with open(listPath, "r") as listIn:
		for email in listIn:
			badDomain = True

			for domainName in domainList:
				if domainName in email.lower():
					badDomain = False

			if badDomain == False:
				mailData.append(email.rstrip().lower())


	newList = []
	for email in mailData:
		cleanEmail = email.split(":", 1)[0]
		cleanEmail = cleanEmail.split(";", 1)[0]
		
		if cleanEmail not in newList:
			newList.append(cleanEmail)

	random.shuffle(newList)
	print(str(len(newList)) + " Unique emails extracted.")

	with open(os.getcwd() + "/domains_extracted.log", "a") as fileOut:
		for email in newList:
			fileOut.write(email + "\n")



if __name__ == "__main__":
	try:
		fileName = sys.argv[1]
		domainList = sys.argv[2].split(",")
		main(fileName, domainList)
	except:
		print("Usage: python3 extract_domains.py filename.log domain.com")