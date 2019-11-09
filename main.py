import os
from dotenv import load_dotenv
from gmail.gmail import create_message, send_message
from image.hcti import create_score_image
from score.score import read_valid_scores


def send_email(to, image_url):
  with open('email.html') as f:
    email = f.read()

  email = email.replace('{image}', image_url)

  msg = create_message('', to, os.getenv('EMAIL_TITLE'), email)
  send_message(os.getenv('EMAIL_SENDER'), msg)


load_dotenv()
scores = read_valid_scores(os.getenv('SCORE_CSV_PATH'))

for score in scores:
  print('# Process.. %s' % score['name'])
  image_url = create_score_image(score)
  print('url %s' % image_url)
  send_email(score['email'], image_url)
