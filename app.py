from flask import Flask, request, jsonify
import flask
from flask_restful import Resource, Api
from service.views import views
from data.sw_facility_dao import SolidWasteFacilityDao


def create_app():
    _app = Flask(__name__, template_folder='template', static_url_path='', static_folder='static',)
    _app.config['APP_NAME'] = 'Recycling Aide'
    _app.register_blueprint(views, url_prefix='/')
    return _app


app = create_app()
api = Api(app)
dao = SolidWasteFacilityDao()


class GetWasteTypes(Resource):
    def get(self):
        return jsonify(SolidWasteFacilityDao.get_waste_types())


class GetActivities(Resource):
    def get(self):
        return jsonify(SolidWasteFacilityDao.get_activities())


class GetFacilityList(Resource):
    def get(self):
        res = dao.get_all_facilities()
        return jsonify(res)


class GetNearestFacilityList(Resource):
    def get(self, lat, lng, topn, waste_type, activity):
        res = dao.get_nearest_facilities(float(lat), float(lng), int(topn), str(waste_type), str(activity))
        return jsonify(res)


api.add_resource(GetWasteTypes, '/get_waste_types')
api.add_resource(GetActivities, '/get_activities')
api.add_resource(GetFacilityList, '/get_facility_list')
api.add_resource(GetNearestFacilityList, '/get_nearest_facility_list/<lat>,<lng>,<topn>,<waste_type>,<activity>')


@app.before_request
def before_request():
    flask.g.site_url = "%s%s" % ( request.host, request.script_root )
    flask.g.recycling_aide = "Recycling Aide"
    flask.g.slogan = "Recycling Right!"


if __name__ == '__main__':
    app.run(debug=True)


## http://127.0.0.1:5000/get_waste_types
## http://127.0.0.1:5000/get_activities
## http://127.0.0.1:5000/get_facility_list
## http://127.0.0.1:5000/get_nearest_facility_list/35.95954153292285,-79.06147683764769,5,HHW,All
