from bleach import clean

whitelist = ["ul", "li", "ol", "strong", "b", "br"]
def clean_spaces_and_newlines(scr):
    result= re.findall("\w+[,.!]?\\n?|<\w+>\\n?|</\w+>\\n?", src)
    return result

with open("page.html","r", encoding="utf-8") as html_file:
    html = html_file.read()
    html_cleaned = clean(html, strip=True)
    html_cleaned = clean_spaces_and_newlines(html_cleaned)
    html_cleaned = " ".join(html_cleaned)
    print(html_cleaned)

with open("out/cleaned_text.txt","w", encoding="utf-8") as outfile:
    outfile.write(html_cleaned)