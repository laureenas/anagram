from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from application import db
from services.models import LETTER_COUNT_EN


class Corpus(db.Model):
    '''Class that represents corpus of words'''

    __tablename__ = 'corpus'

    word = mapped_column(String(), unique=True, nullable=False, primary_key=True)
    word_length = mapped_column(Integer, nullable=False)
    letter_map = mapped_column(String(LETTER_COUNT_EN), nullable=False)
