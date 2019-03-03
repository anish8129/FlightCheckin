from flask import Flask,url_for,redirect,render_template,request,jsonify
import simplejson as json
import requests
from Dto_Classes import Reservation,ReservationUpdateRequest,Flight,Passenger


app=Flask(__name__)

url='http://localhost:8080/reservations/'

@app.route('/')
def flightCheckin():
    return render_template('checkin.html')


@app.route('/startCheckin',methods=['POST'])
def startCheckin():
    if request.method=='POST':
        val=request.form['reservation_id']
        test=url+val
        resp=requests.get(test)
        if resp.status_code ==200:
            obj=resp.json()
            passenger=Passenger(obj['passenger']['id'],obj['passenger']['f_name'],obj['passenger']['l_name'],
            obj['passenger']['email'],obj['passenger']['phone'])
            
            flight=Flight(obj['flight']['id'],obj['flight']['flight_no'],
            obj['flight']['operating_airlines'],obj['flight']['departure_city'],
            obj['flight']['arrival_city'],obj['flight']['departure_date']
            ,obj['flight']['estimated_departure_time'])

            reservation=Reservation(obj['id'],obj['checked_in'],obj['number_of_bags'],passenger,flight)
            return render_template('displayDetails.html',reservation=reservation)


@app.route('/completeCheckin',methods=['POST'])
def completeCheckin():
    if request.method=='POST':
        updatereq={'id':request.form['reservation_id'], 'checked_in': '1','number_of_bags' :request.form['number_of_bags']}
        data= json.dumps(updatereq)
        print(data)
        resp=requests.post(url,json={'id':updatereq['id'],'checked_in': updatereq['checked_in'] ,'number_of_bags' : updatereq['number_of_bags']})
        print(resp.json())
        if resp.status_code==200:
            obj=resp.json()
            passenger=Passenger(obj['passenger']['id'],obj['passenger']['f_name'],obj['passenger']['l_name'],
            obj['passenger']['email'],obj['passenger']['phone'])
            
            flight=Flight(obj['flight']['id'],obj['flight']['flight_no'],
            obj['flight']['operating_airlines'],obj['flight']['departure_city'],
            obj['flight']['arrival_city'],obj['flight']['departure_date']
            ,obj['flight']['estimated_departure_time'])

            reservation=Reservation(obj['id'],obj['checked_in'],obj['number_of_bags'],passenger,flight)        
            return render_template('completeReservation.html',reservation=reservation)
    return None

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000,threaded=False)
