import requests
from bs4 import BeautifulSoup

url = 'https://www.digitalgujarat.gov.in/loginapp/CitizenLogin.aspx'
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')

tr_tags = soup.find_all('tr')

# Loop through each <tr> tag and extract the text and links from the specified structure
for tr_tag in tr_tags:
    # Find all <td> tags inside the current <tr> tag
    td_tags = tr_tag.find_all('td')
    # Check if there are at least 2 <td> tags
    if len(td_tags) >= 2:
        # Find the <span> tag inside the 2nd <td> tag
        span_tag = td_tags[1].find('span')
        # Check if <span> tag is found
        if span_tag:
            # Find all <a> tags inside the <span> tag
            a_tags = span_tag.find_all('a')
            # Check if there are at least 2 <a> tags
            if len(a_tags) >= 2:
                # Extract text from the 2nd <a> tag
                text = a_tags[1].text.strip()
                # Get the href attribute if it exists, otherwise set it to an empty string
                href = a_tags[1].get('href', '').strip()
                # Initialize an empty string to store the formatted text and links
                formatted_text = f"~^\\{text}#~!~#{url + href}~^\\"
                # Loop through subsequent <a> tags and concatenate their text and links in the desired format
                for a_tag in a_tags[2:]:
                    link_text = a_tag.text.strip()
                    # Get the href attribute if it exists, otherwise set it to an empty string
                    link_href = a_tag.get('href', '').strip()
                    if link_href:
                        # Format the hyperlink in the desired format
                        formatted_link = f"~^\\{link_text}#~!~#{url + link_href}~^\\"
                    else:
                        formatted_link = f"~^\\{link_text}#~!~#~^\\"
                    # Concatenate formatted text and links
                    formatted_text += formatted_link
                print(formatted_text)
