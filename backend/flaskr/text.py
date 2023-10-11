from flask import ( Blueprint, request, jsonify )


from towhee import DataCollection

from flaskr.utils.search_text import search_pipe

bp = Blueprint('text', __name__, url_prefix='/text')

@bp.route('', methods=('GET', 'POST'))
def search():
    text_search = request.args.get('text')
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
