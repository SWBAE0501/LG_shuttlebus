from app import create_app
from models import db, BusStop, BusRoute

app = create_app()
app.app_context().push()

db.create_all()

# 예제 데이터 삽입
stops = [
    BusStop(name="정류장 1", latitude=37.5665, longitude=126.9780),
    BusStop(name="정류장 2", latitude=37.5700, longitude=126.9820),
    BusStop(name="정류장 3", latitude=37.5735, longitude=126.9860),
    BusStop(name="정류장 4", latitude=37.5770, longitude=126.9900)
]

routes = [
    BusRoute(route_order=1, latitude=37.5665, longitude=126.9780),
    BusRoute(route_order=2, latitude=37.5700, longitude=126.9820),
    BusRoute(route_order=3, latitude=37.5735, longitude=126.9860),
    BusRoute(route_order=4, latitude=37.5770, longitude=126.9900)
]

db.session.bulk_save_objects(stops)
db.session.bulk_save_objects(routes)
db.session.commit()
