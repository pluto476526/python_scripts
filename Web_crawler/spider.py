import requests
from bs4 import BeautifulSoup
import csv
import os

def fetch_html(url, elements) :
	try :	
		response = requests.get(url)
		
		if response.status_code == 200:
			soup = BeautifulSoup(response.text, 'html.parser')

			# Extract title
			title = soup.title.string.strip() if soup.title else 'webpage'

			# Clean title
			filename = "".join([c if c.isalnum() or c == '_' else "_" for c in title.replace(' ', '_')]) + '.csv'

			# Open CSV file
			with open(filename, mode='w', newline='', encoding='utf-8') as file :
				writer = csv.writer(file)
				writer.writerow(['Tag', 'Content'])

				# Loop through tags
				for element in elements :
					stuffs = soup.find_all(element)
				
					if stuffs :
						print(f"\nFound {len(stuffs)} <{element}> tags:")
						
						for stuff in stuffs :
							stuff_txt = stuff.text.strip() if element != 'a' else stuff.get('href', '')
							print(f"<{element}>: {stuff_txt}")
							writer.writerow([element, stuff_txt])
					else :
						print(f"No <{element}> tags found.")
			print(f"\nData saved to '{filename}'")
		else :
			print(f"Failed to retrieve with status code: {response.status_code}")
	except requests.exceptions.RequestException as e :
		print(f"An error occurred: {e}")

# Get URL
url = input("Enter URL: ")

# Split input into list
elements_in = input("Enter tag (comma-separated): ")
elements = [element.strip() for element in elements_in.split(',')]

fetch_html(url, elements)

