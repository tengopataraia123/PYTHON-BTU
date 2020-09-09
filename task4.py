from flask_sqlalchemy import SQLAlchemy

datab= SQLAlchemy()

class Currency(datab.Model):
    id = datab.Column(datab.Integer)
    cur_name = datab.Column(datab.String(3))
    rate = datab.Column(datab.FLOAT)

    def __str__(self):
        return f'{self.id}{self.cur_name}{self.rate}'

ob=(Currency(1,'EUR',3.45)