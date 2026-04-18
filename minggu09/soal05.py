import re
from datetime import datetime as waktu

kata = """Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, 
seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."""

hari = waktu.now()

for t in re.finditer(r'(\d{4})-(\d{2})-(\d{2})', kata):
    thn, bln, tgl = map(int,t.groups())
    tanggal = waktu(thn, bln, tgl)
    selisih = (hari - tanggal).days
    print(f"{thn}-{bln:02d}-{tgl:02d} 00:00:00 selisih {selisih} hari")