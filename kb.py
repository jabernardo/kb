import glob
import re

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
  content = []

  if matches:
    for match in matches:
      code = parse_markdown_data(match[1])

      if code:
        content.append({
          "title": match[0],
          "language": code["language"],
          "code": code["gist"]
        })

  return content

def get_info(keyword):
  info = []

  for md in get_markdowns():
    try:
      with open(md) as kb:
        data = parse_markdown(kb.read())

        for content in data:
          if keyword in content["title"] or keyword in content["code"]:
            info.append(content)

        kb.close()
    except Exception as ex:
      print(ex)

  return info

def main():
  keyword = input("Search: ")
  infos = get_info(keyword)

  for info in infos:
    print(f"{ '=' * 80 }\n{info['title']} (in {info['language']})")
    print(f"{ '=' * 80 }\n{ info['code'].strip() }\n{ '=' * 80 }\n")

if __name__ == "__main__":
  main()
