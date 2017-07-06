from flask import Flask

app = Flask(__name__)
words = ['flask', 'blessed']
words_dictionary = {'flask': {'definition': ['noun. a container or bottle'],
                   'example': ['his silver flask of brandy'],
                   'synonym': ['beaker', 'bottle', 'fiasco', 'jar'],
                   'antonym': []},
         'blessed': {'definition': ['adjective. made holy; consecrated',
                                    'noun. those who live with God in heaven'],
                     'example': ['there was not a blessed thing anybody chould have done'],
                     'synonym': ['adored', 'divine', 'holy', 'glorified'],
                     'antonym': ['condemned', 'cursed', 'damned', 'disapproved']}}

@app.route('/')
def index():
    return '<h1>Word Master</h1>'


@app.route('/master/<int:id>')
def master(id):
    return ('<h1>Word Master</h1>'
            '<p>Word: {0}</p


if __name__ == '__main__':
    app.run(debug=True)
