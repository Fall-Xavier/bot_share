import requests, json
ses=requests.Session()

cok = input(" masukan cookie : ")
token = input(" masukan token : ")
idt = input(" masukan link : ")
limit = int(input(" masukan limit : "))
cookie = {"cookie":cok}
try:
	n = 0
	header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
	for x in range(limit):
		n+=1
		post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).text
		data = json.loads(post)
		if "id" in post:
			print(f" {n}. berhasil membagikan {data['id']}")
		else:
			exit(" gagal membagikan, kemungkinan token invalid")
except:
	exit(" gagal membagikan, kemungkinan token invalid")
