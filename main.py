from gmail.gmail import create_message, send_message
from score.score import read_valid_scores
from image.hcti import create_score_image

def send_email(to, image_url):
  with open('email.html') as f:
    email = f.read()

  email = email.replace('{image}', image_url)

  msg = create_message('', to, 'Play O Ground 보은 경기 결과(Play O Ground Result)', email)
  send_message('orienteeringlovers@gmail.com', msg)


scores = read_valid_scores('score/sample.csv')

for score in scores:
  print('# Process.. %s' % score['name'])
  image_url = create_score_image(score)
  print('url %s' % image_url)
  send_email(score['email'], image_url)
