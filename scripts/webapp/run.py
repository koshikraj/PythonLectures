
from sanic import Sanic
from sanic.response import json
from models import Participant

app = Sanic()

@app.route('/participant', methods=['GET', 'POST', 'DELETE'])
async def get_handler(request):
    participant = Participant()
    if request.method == 'GET':
        participant_list = participant.list_participants()

        return json({'data': participant_list})
    elif request.method == 'POST':
        participant_ins = request.json
        participant.create_participant(name=participant_ins['name'],
                                      age=participant_ins['age'],
                                      city=participant_ins['city'])
        return json({'status': True})
    else:
        return json({'status': False, 'message': 'method not implemented'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)