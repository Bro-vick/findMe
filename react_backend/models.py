from exts import db


class Profile(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(25),nullable=False,unique=True)
    user_bio=db.Column(db.Text(),nullable=False)
    picture_url=db.Column(db.String(),nullable=False)
    twitter=db.Column(db.String(),nullable=False)
    github=db.Column(db.String(),nullable=False)
    linkedin=db.Column(db.String(),nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self,username,user_bio,picture_url,twitter,github,linkedin):
        self.username=username
        self.user_bio=user_bio
        self.picture_url=picture_url
        self.twitter=twitter
        self.github=github
        self.linkedin=linkedin

        db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        """
        returns string rep of object
        """
        return f"<User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()