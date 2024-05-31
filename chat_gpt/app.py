from flask import Flask, render_template
import folium
from config import Config
from models import db, BusStop, BusRoute

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route('/')
    def index():
        # 지도 생성 (서울을 중심으로 설정)
        map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

        # 셔틀버스 정류장 불러오기
        bus_stops = BusStop.query.all()

        # 정류장을 지도에 추가
        for stop in bus_stops:
            folium.Marker(
                location=[stop.latitude, stop.longitude],
                popup=stop.name,
                icon=folium.Icon(icon="cloud")
            ).add_to(map)

        # 셔틀버스 경로 불러오기
        bus_routes = BusRoute.query.order_by(BusRoute.route_order).all()

        # 경로를 폴리라인으로 지도에 추가
        route_coordinates = [[route.latitude, route.longitude] for route in bus_routes]
        folium.PolyLine(route_coordinates, color="blue", weight=2.5, opacity=1).add_to(map)

        # 지도를 HTML 파일로 저장
        map.save('templates/map.html')
        
        return render_template('map.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
