# 오리엔티어링 기록 이메일 발송(Send Orienteering Score image)

## Setup

### Copy `.env` template
``` bash
cp .evn.example .env
```

### Fill the values in `.env` accordingly.
1. Go https://htmlcsstoimage.com/ and get an API key and User ID. Then fill the values below.
```
HCTI_API_USER_ID= 
HCTI_API_KEY= 
```

2. Download Gmail API Credential file and set the file path. Follow this guide(https://developers.google.com/gmail/api/quickstart/python)
```
GMAIL_CREDENTIALS_PATH=
```

3. Set the path of score csv file.
- CSV format: Number,Class,Rank,Course,Name1,Name2,Club1,Club2,Country1,Country2,Age,Sex,Card Number,Card Memo,Activate/Check Time,Start Time,Finish Time,Result,Category,Class,Email
```
SCORE_CSV_PATH=
```