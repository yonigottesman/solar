from app import app, db
from app.models import Body, Delta


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Body': Body, 'Delta': Delta}
