from flask import ( Blueprint, Response, request, jsonify )


from towhee import DataCollection

from flaskr.utils.search_text import search_pipe

bp = Blueprint('text', __name__, url_prefix='/text')

@bp.route('', methods=('GET', 'POST'))
def search():
    text_search = request.args.get('text')
    print(text_search)
    if not text_search:
        return jsonify({"message": "Please Input Text",}), 400
    res = search_pipe(text_search)
    result = []
    for r in  DataCollection(res).to_list():
        result.append({
            "id": r.id,
            "title": r.title,
            "score": r.score
        })
    return { "result":  result }
