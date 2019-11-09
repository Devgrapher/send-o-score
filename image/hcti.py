import os
import requests
from dotenv import load_dotenv

load_dotenv()

IMAGE_FORMAT='.jpg'

def _create_image(html, css, score):
  HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
  HCTI_API_USER_ID = os.getenv('HCTI_API_USER_ID')
  HCTI_API_KEY = os.getenv('HCTI_API_KEY')

  data = {
    'html': html,
    'css': css,
  }

  image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

  return image.json()['url'] + IMAGE_FORMAT


def create_score_image(score):
  with open(os.getenv('IMAGE_HTML_PATH')) as f:
    html = f.read()
  with open(os.getenv('IMAGE_CSS_PATH')) as f:
    css = f.read()

  html = html.replace('{name}', score['name'])
  html = html.replace('{category}', score['category'])
  html = html.replace('{class}', score['class'])
  html = html.replace('{result}', score['result'])

  return _create_image(html, css, score)


if __name__ == "__main__":
  score = {
    'name': '김지훈',
    'category': 'Sprint',
    'class': 'M21E',
    'result': '20:11',
  }
  url = create_score_image(score)
  print("image URL: %s" % url)
