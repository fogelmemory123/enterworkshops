from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from flask_jwt_extended import JWTManager
from resources import (EventResource, BirthDayResource, GetUserName,
                        LoginResource, RegisterResource, BranchResource,
                        AdminBirthDayResource, AdminBranchResource,
                        AdminEventResource,RegisterParticipantResource,EventParticipantsResource,EventDetailResource)
from flask_cors import CORS
from extensions import mail



app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["*"])

app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)
mail.init_app(app)  # יצירת אובייקט Flask-Mail ברמה גלובלית

db.init_app(app)

with app.app_context():
    db.create_all()



api.add_resource(BirthDayResource, '/birthdays')
api.add_resource(EventResource, '/events')
api.add_resource(LoginResource, '/login')
api.add_resource(RegisterResource, '/register')
api.add_resource(BranchResource, '/branches')
api.add_resource(AdminBirthDayResource, '/admin/birthdays')
api.add_resource(AdminBranchResource, '/admin/branches')
api.add_resource(AdminEventResource,"/admin/events")
api.add_resource(GetUserName,"/username")
api.add_resource(EventDetailResource, '/api/events/<int:event_id>')

api.add_resource(RegisterParticipantResource, '/api/events/register')  # Register the resource
api.add_resource(EventParticipantsResource, '/api/events/<int:event_id>/participants/<int:participant_id>')
if __name__ == '__main__':
    app.run(debug=True)

