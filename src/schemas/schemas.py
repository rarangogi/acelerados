from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from database.models import BlackListModel


class BlackListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BlackListModel
        include_relationships = True
        load_instance = True
