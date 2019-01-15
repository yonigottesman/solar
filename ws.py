import telnetlib
import time

HOST = 'horizons.jpl.nasa.gov'
PORT = 6775

tn = telnetlib.Telnet(HOST, PORT)


print(tn.read_until(b'Horizons>').decode('ascii'))
tn.write(b'Mars\n')
print(tn.read_until(b'<cr>:').decode('ascii'))
tn.write(b'499\n')
print(tn.read_until(b'<cr>:').decode('ascii'))
tn.write(b'E\n')
print(tn.read_until(b'[o,e,v,?] :').decode('ascii'))
tn.write(b'o\n')
print(tn.read_until(b'[ <id>,coord,geo  ] :').decode('ascii'))
tn.write(b'\n')
print(tn.read_until(b'1600-Jan-01 00:00] :').decode('ascii'))
tn.write(b'2019-Jan-15 00:00\n')
print(tn.read_until(b'2500-Jan-03 23:58] :').decode('ascii'))
tn.write(b'2019-Jan-17 00:00\n')
print(tn.read_until(b' [ex: 10m, 1h, 1d, ? ] :').decode('ascii'))
tn.write(b'1h\n')
print(tn.read_until(b'Accept default output [ cr=(y), n, ?] :').decode('ascii'))




