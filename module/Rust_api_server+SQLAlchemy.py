from os.path import join

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///department.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class department_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    schudule = db.Column(db.String(8), nullable=True)
    route_length = db.Column(db.Float, nullable=True)
    travel_time = db.Column(db.Float, nullable=True)
    route = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f"Video(Train Num = {self.num},Capacity = {self.capacity}, Schudule = {self.schudule}, " \
               f"Route length = {self.route_length}, Travel Time = {self.travel_time}," \
               f"Route = {self.route})"


dep_put_args = reqparse.RequestParser()
dep_put_args.add_argument("num", type=int, help="Number of the video is required", required=True)
dep_put_args.add_argument("capacity", type=int, help="Number of the video is required", required=True)
dep_put_args.add_argument("schudule", type=str, help="Schudule of the route is required", required=True)
dep_put_args.add_argument("route_length", type=float, help="Route length of the route is required", required=True)
dep_put_args.add_argument("travel_time", type=float, help="Travel Time of the route is required", required=True)
dep_put_args.add_argument("route", type=str, help="Route of the route is required", required=True)

# video_update_args = reqparse.RequestParser()
# video_update_args.add_argument("num", type=int, help="Number of the video is required", required=True)
# video_update_args.add_argument("capacity", type=int, help="Number of the video is required", required=True)
# video_update_args.add_argument("schudule", type=str, help="schudule of the route", required=True)
# video_update_args.add_argument("route_length", type=float, help="Route length of the route", required=True)
# video_update_args.add_argument("travel_time", type=float, help="Travel Time of the route", required=True)
# video_update_args.add_argument("route", type=str, help="Route of the route", required=True)

resource_fields = {
    'id': fields.Integer,
    'num': fields.Integer,
    'capacity': fields.Integer,
    'schudule': fields.String,
    'route_length': fields.Float,
    'travel_time': fields.Float,
    'route': fields.String
}


class Main(Resource):
    @marshal_with(resource_fields)
    def get(self, num):
        if num == 0:
            result = department_db.query.filter_by().all()
        else:
            if not department_db.query.filter_by(id=num).first():
                abort(404, message="Could not find transport with that id")
            result = department_db.query.filter_by(num=num).first()
        return result

    @marshal_with(resource_fields)
    def put(self,num):
        if department_db.query.filter_by(id=num).first():
            abort(409, message="Id taken...")
        args = dep_put_args.parse_args()
        data = department_db(id=num,num=args['num'], capacity=args['capacity'],
                             schudule=args['schudule'], route_length=args['route_length'],
                             travel_time=args['travel_time'], route=args['route'])
        db.session.add(data)
        db.session.commit()
        return data, 201


# @marshal_with(resource_fields)
# def patch(self, num):
#     args = video_update_args.parse_args()
#     result = department_db.query.filter_by(id=num).first()
#     if not result:
#         abort(404, message="Video doesn't exist, cannot update")
#
#     if args['num']:
#         result.name = args['name']
#     if args['views']:
#         result.views = args['views']
#     if args['likes']:
#         result.likes = args['likes']
#
#     db.session.commit()
#
#     return result

class support_get_last(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return department_db.query.order_by(None).order_by(department_db.id.desc()).first()


@app.route('/create')
def create():
    with app.app_context():
        db.create_all()
    return {200: "Tables created!"}


api.add_resource(Main, "/num/<int:num>")
api.add_resource(support_get_last, "/get_last")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)



# from Desing_Patterns.module.SQLAlchemy import app,db
# with app.app_context():
#     db.create_all()
