from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

events = [
    {"id": 1, "name": "Band Night", "date": "2024-05-01", "description": "Live band performance"},
    {"id": 2, "name": "DJ Party", "date": "2024-05-02", "description": "Electronic music night"},
]

taken_seats = {1: [1, 2, 3], 2: [5, 6]}  # example taken seats per event

@app.route('/')
def home():
    return render_template('home.html', events=events)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/event/<int:event_id>')
def event(event_id):
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return "Event not found", 404
    seats = []
    for row in range(1, 11):
        for col in range(1, 11):
            seat_id = (row - 1) * 10 + col
            taken = seat_id in taken_seats.get(event_id, [])
            seats.append({"id": seat_id, "row": row, "col": col, "taken": taken})
    return render_template('event.html', event=event, seats=seats)

@app.route('/buy/<int:event_id>/<int:seat_id>', methods=['POST'])
def buy(event_id, seat_id):
    if seat_id in taken_seats.get(event_id, []):
        return "Seat already taken", 400
    taken_seats.setdefault(event_id, []).append(seat_id)
    event = next((e for e in events if e['id'] == event_id), None)
    return render_template('confirmation.html', event=event, seat_id=seat_id)

if __name__ == '__main__':
    app.run(debug=True)