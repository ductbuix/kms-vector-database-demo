import os

from flask import ( Blueprint, request, jsonify )
from langchain import hub
from langchain.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader
from langchain.vectorstores import Milvus
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
from langchain.callbacks.manager import CallbackManager
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
import validators

from flaskr import TXT_ALLOWED_EXTENSIONS, PDF_ALLOWED_EXTENSIONS, TXT_UPLOAD_FOLDER, PDF_UPLOAD_FOLDER
from werkzeug.utils import secure_filename

bp = Blueprint('docs', __name__, url_prefix='/docs')
QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-llama")
llm = Ollama(model="llama2",
             verbose=True,
             callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
embeddings = OllamaEmbeddings(base_url="http://localhost:11434", model="llama2")
milvus_collection = ['web', 'txt', 'pdf']


def pdf_allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in PDF_ALLOWED_EXTENSIONS


def txt_allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in TXT_ALLOWED_EXTENSIONS


@bp.route('/import-pdf', methods=['POST'])
def import_pdf():
    if 'file' not in request.files:
        return jsonify({ "message": "Please Input File in Form Data" }), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({ "message": "Filename cannot be blank"}), 400

    if file and pdf_allowed_file(file.filename):
        filename = secure_filename((file.filename))
        pdf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), PDF_UPLOAD_FOLDER, filename)
        file.save(pdf_path)
        loader = PyPDFLoader(pdf_path)
        docs = loader.load_and_split()
        
        Milvus.from_documents(
            docs,
            embeddings,
            collection_name = 'pdf',
            connection_args={"host": "127.0.0.1", "port": "19530"},
        )
        return { "result": "Success" }
    else:
        return jsonify({ "message": "File is not allowed"}), 400
    

@bp.route('/import-txt', methods=['POST'])
def import_txt():
    if 'file' not in request.files:
        return jsonify({ "message": "Please Input File in Form Data" }), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({ "message": "Filename cannot be blank"}), 400

    if file and txt_allowed_file(file.filename):
        filename = secure_filename((file.filename))
        txt_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), TXT_UPLOAD_FOLDER, filename)
        file.save(txt_file_path)
        loader = TextLoader(txt_file_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        
        Milvus.from_documents(
            docs,
            embeddings,
            collection_name = 'text',
            connection_args={"host": "127.0.0.1", "port": "19530"},
        )
        return { "result": "Success" }
    else:
        return jsonify({ "message": "File is not allowed"}), 400


@bp.route('/import-web', methods=['POST'])
def import_web():
    web_link = request.json.get('url')
    if not web_link:
        return jsonify({ "message": "Please Input Web Link", }), 400
    if not validators.url(web_link):
        return jsonify({ "message": "Link is not valid" })
    loader = WebBaseLoader(web_link)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    docs = text_splitter.split_documents(data)
    Milvus.from_documents(
        docs,
        embeddings,
        collection_name = 'web',
        connection_args={"host": "127.0.0.1", "port": "19530"},
    )
    return { "result": "Success" }


@bp.route('/retrieve', methods=['GET'])
def retrieve():
    question = request.args.get('question')
    if not question:
        return jsonify({ "message": "Please input your question",}), 400

    collection_name = request.args.get('collection_name')
    if not collection_name:
        return jsonify({ "message": "Please input the Milvus collection name" })
    if collection_name not in milvus_collection:
        return jsonify({ "message": "collection_name must be in ['txt', 'web', 'pdf']"})

    vector_db = Milvus(
        embedding_function=embeddings,
        collection_name = collection_name,
        connection_args={"host": "127.0.0.1", "port": "19530"}
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vector_db.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )
    result = qa_chain({"query": question})
    return {"result": result}
