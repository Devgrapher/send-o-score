import requests

def _create_image(html, css, score):
  HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
  HCTI_API_USER_ID = 'ad100bbc-6b53-40ca-aa89-20f136d920de'
  HCTI_API_KEY = '43d25aef-cc81-44da-b269-9e1658925642'

  data = {
    'html': html,
    'css': css,
  }

  image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

  return image.json()['url']


def create_score_image(score):
  with open('image/score.html') as f:
    html = f.read()
  with open('image/score.css') as f:
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
