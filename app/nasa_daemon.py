import telnetlib
import time
from datetime import datetime, timedelta



def get_spac_deltas(body_id, start_date, end_date):

    HOST = 'horizons.jpl.nasa.gov'
    PORT = 6775
    tn = telnetlib.Telnet(HOST, PORT)

    tn.read_until(b'Horizons>')
    tn.write(str.encode(str(body_id)+'\n'))

    tn.read_until(b'<cr>:')
    tn.write(b'e\n')

    tn.read_until(b'[o,e,v,?] :')
    tn.write(b'o\n')

    tn.read_until(b'[ <id>,coord,geo  ] :')
    tn.write(b'coord\n')

    tn.read_until(b'Cylindrical or Geodetic input [ c,g ] :')
    tn.write(b'g\n')

    tn.read_until(b'Specify geodetic {E. Long, lat, h } :')
    matam_coordinates = b'34.959351,32.789973,0\n'
    tn.write(matam_coordinates)

    tn.read_until(b'Starting UT  [>=   1600-Jan-01 00:00] :')
    tn.write(str.encode(str(start_date)+'\n'))

    tn.read_until(b'Ending   UT  [<=   2500-Jan-03 23:58] :')
    tn.write(str.encode(str(end_date)+'\n'))

    tn.read_until(b'Output interval [ex: 10m, 1h, 1d, ? ] :')
    tn.write(b'1m\n')

    tn.read_until(b'Accept default output [ cr=(y), n, ?] :')
    tn.write(b'\n')

    tn.read_until(b'Select table quantities [ <#,#..>, ?] :')
    tn.write(b'20\n')

    tn.read_until(b'$$SOE')
    ret = tn.read_until(b'$$EOE').decode('ascii')
    # print(ret)
    return ret


def update_deltas(body):
    from app.models import Body, Delta
    from app import db
    utc_now = datetime.utcnow()
    utc_future = utc_now+timedelta(hours=1)
    deltas = get_spac_deltas(499, utc_now.strftime("%Y-%b-%d %H:%M"),
                             utc_future.strftime("%Y-%b-%d %H:%M"))
    
    current = body.deltas.all()
    current_times = {d.time for d in current}
    for delta in deltas.split('\n'):
        line = delta.split()
        if len(line) == 5:
            date = datetime.strptime(line[0]+' ' + line[1], '%Y-%b-%d %H:%M')
            if date in current_times:
                pass
            else:
                au = line[3]
                delta = Delta(time=date, au=au, body=body)
                db.session.add(delta)
    db.session.commit()

    # now delete older values
    Delta.query.filter(Delta.time < datetime.utcnow()).delete()
    db.session.commit()

def tick():
    from app.models import Body, Delta
    print('Tick')
    for body in Body.query.all():
        update_deltas(body)
