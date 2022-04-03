import logging

from flask import request
from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

from schemas.schemas import BlackListSchema
from settings import APP, basic_auth_users

black_list_schema = BlackListSchema()
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in basic_auth_users and check_password_hash(
            basic_auth_users.get(username), password
    ):
        return username


class Health(Resource):
    def get(self):
        return {"status": "ok"}, 200

#
# class GetBlackList(Resource):
#     @auth.login_required
#     def get(self, email: str) -> dict:
#         logging.info(f'{APP} logger Get Black List:'
#                      f'start for email {email}')
#         session = create_session(engine_object=engine)
#         black_list = session.query(BlackListModel).filter(
#             BlackListModel.email == email
#         ).first()
#         response = black_list_schema.dump(black_list)
#         session.remove()
#         logging.info(f'{APP} logger Get Black List:'
#                      f'done for email {email} '
#                      f'response {response}')
#         return response
#
#
# class PostBlackList(Resource):
#     @auth.login_required
#     def post(self) -> dict:
#         data = request.get_json(force=True)
#         logging.info(f'{APP} logger Post Black List:'
#                      f'start for {data}')
#         data["ip"] = request.remote_addr
#         session = create_session(engine_object=engine)
#         save_to_db(session=session, db_model=BlackListModel(
#             **data
#         ))
#         session.remove()
#         logging.info(f'{APP} logger Post Black List:'
#                      f'done for {data}')
#         return data
