import smtplib
from email.mime.text import MIMEText

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작
s.starttls()

#로그인 인증
s.login('email', 'pwd')

#보낼 메시지 설정
msg = MIMEText("내용 : 본문내용 테스트입니다.")
msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'
msg['From'] = '@gmail.com'
msg['To'] = '@gmail.com'


#메일보내기
s.sendmail("@gmail.com", "@gmail.com", msg.as_string())

#세션 종료
s.quit()
