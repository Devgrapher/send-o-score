import csv
import os
from dotenv import load_dotenv

load_dotenv()

def read_csv(path):
  players=[]
  with open(path) as f:
    read = csv.reader(f)
    read.__next__() # skip header
    for row in read:
      player = {
        'name': row[4],
        'start': row[15],
        'finish': row[16],
        'result': row[17],
        'category': row[18],
        'class': row[19],
        'email': row[20],
      }
      players.append(player)
  return players

def filter_valid_scores(player):
  if player['name'] and player['result'] and player['category'] and player['email']:
    if player['result'] == 'DNS' or player['result'] == 'DISQ':
      return None
    return player

  return None

def read_valid_scores(path):
  players = read_csv(path)
  return list(filter(filter_valid_scores, players))

if __name__ == "__main__":
  players = read_valid_scores(os.getenv('SCORE_CSV_PATH') or 'sample.csv')
  print(players)
