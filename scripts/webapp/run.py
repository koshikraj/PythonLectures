
from sanic import Sanic
from sanic.response import json
from models import Participant

app = Sanic()

@app.route('/participant', methods=['GET', 'POST'])
async def get_handler(request):
    participant = Participant()
    if request.method == 'GET':
        participant_list = participant.list_participants()

        return json({'data': participant_list})
    else:
        participant.creat_participant(name='Koshik',
                                      age=25,
                                      city='Bangalore')
        return json({'status': True})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)