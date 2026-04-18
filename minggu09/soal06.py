import re
import random
import string

kata = """Berikut adalah daftar email dan nama pengguna dari mailing list:
chei@mail.com dimiliki oleh cheila
cia@gmail.co.id dimiliki oleh alicia
yebe@getnada.com dimiliki oleh reza
acoy@tokopedia.com dimiliki oleh toko matahari"""

for c in re.findall(r'(\w+@[\w.]+)', kata):
    username = c.split('@')[0]
    pw = ''.join(random.choices(string.ascii_letters + string.digits, k = 8))
    print(f"{c}@ username: {c}, password: {pw}")