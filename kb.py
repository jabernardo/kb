import glob
import re
from difflib import SequenceMatcher

def get_markdowns():
  return glob.glob("*/*.md")

def parse_markdown_data(text):
  data = {}

  regex_content = r"^```(\w+)([^`]+)```$"
  matches_content = re.findall(regex_content, text, flags = re.MULTILINE)

  if matches_content:
    return {
      "language": matches_content[0][0],
      "gist": matches_content[0][1]
    }

  return None

def parse_markdown(text):
  regex = r"^## (.*)\s+([^#]+)\s+$"
  matches = re.findall(regex, text, flags = re.MULTILINE)
  content = {}

  if matches:
    for match in matches:
      code = parse_markdown_data(match[1])

      if code:
        content[match[0]] = {
          "language": code["language"],
          "code": code["gist"]
        }

  return content

def get_info():
  info = {}

  for md in get_markdowns():
    # try:
    with open(md) as kb:
      data = parse_markdown(kb.read())
      
      for key, content in data.items():
        info[key] = content

      kb.close()
    # except Exception as ex:
    #   print(ex)

  return info

def main():
  keyword = input("Search: ")
  infos = get_info()

  for title, gist in infos.items():
    title_text = f"{title} (in {gist['language']})"

    if SequenceMatcher(None, keyword, title_text).ratio() > 0.1:
      print(f"{ '=' * 80 }\n{ title_text }")
      print(f"{ '=' * 80 }\n{ gist['code'].strip() }\n{ '=' * 80 }\n")

if __name__ == "__main__":
  main()
