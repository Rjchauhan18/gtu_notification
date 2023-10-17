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
            # Initialize an empty list to store formatted text and links
            formatted_content = []
            # Loop through <a> tags and add text or formatted links based on presence of href attribute
            for a_tag in a_tags:
                link_text = a_tag.text.strip()
                link_href = a_tag.get('href', '').strip()
                if link_href:
                    # Format the hyperlink in the desired format
                    formatted_link = f"~^\\{link_text}#~!~#{url + link_href}~^\\"
                    formatted_content.append(formatted_link)
                else:
                    # If no href attribute, add plain text to the formatted content list
                    formatted_content.append(link_text)
            # Join the formatted content list and print
            formatted_text = ' '.join(formatted_content)
            print(formatted_text)
