import telnetlib

HOST = 'horizons.jpl.nasa.gov'
PORT = 6775


def tick():
    tn = telnetlib.Telnet(HOST, PORT)
    print(tn.read_until(b'Horizons>').decode('ascii'))
