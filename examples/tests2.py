
def _init_testdb():
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///")
    engine.echo = True
    from models import Base, Session
    Session.remove()
    Base.metadata.create_all(bind=engine)
    Session.configure(bind=engine)
    return Session

def teardown_module():
    from models import Base, Session
    Session.remove()

def _get_target():
    from models import User
    return User

def _make_one(*args, **kwargs):
    return _get_target()(*args, **kwargs)

def test_it():
    session = _init_testdb()
    user = _make_one(name=u'aodag')
    session.add(user)
    session.commit()

def test_it2():
    session = _init_testdb()
    for i in range(10):
        user = _make_one(name=u'user %d' % i)
        session.add(user)
        session.commit()


def test_none():
    pass
