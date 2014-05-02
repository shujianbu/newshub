from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class articles(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    Title = db.Column(db.String(80), index = True, unique = True)
    Author = db.Column(db.String(40), index = True, unique = True)
    Domain = db.Column(db.String(80), index = True, unique = True)
    URL = db.Column(db.String(200), index = True, unique = True)
    Time_Publish = db.Column(db.DateTime, index = True, unique = True)
    Time_Check = db.Column(db.DateTime, index = True, unique = True)
    ## Not quite sure if the data tyep "db.Text" works. If not, try String 
    Content = db.Column(db.Text, index = True, unique = True)

    def __init__(self, id, title, author, domain, url, time_pub, time_check, content):
        self.ID = id
        self.Title = title
        self.Author = author
        self.Domain = domain
        self.URL = url
        self.Time_Publish = time_pub
        self.Time_Check = time_check

    def __repr__(self):
        return '<User %r>' % (self.url)

class deletions(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    Title = db.Column(db.String(80), index = True, unique = True)
    Author = db.Column(db.String(40), index = True, unique = True)
    Domain = db.Column(db.String(80), index = True, unique = True)
    URL = db.Column(db.String(200), index = True, unique = True)
    Time_Publish = db.Column(db.DateTime, index = True, unique = True)
    Time_Check = db.Column(db.DateTime, index = True, unique = True)
    ## Not quite sure if the data tyep "db.Text" works. If not, try String 
    Content = db.Column(db.Text, index = True, unique = True)

    def __init__(self, id, title, author, domain, url, time_pub, time_check, content):
        self.ID = id
        self.Title = title
        self.Author = author
        self.Domain = domain
        self.URL = url
        self.Time_Publish = time_pub
        self.Time_Check = time_check

    def __repr__(self):
        return '<User %r>' % (self.url)
