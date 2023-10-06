# 1. Set up Vector Database
In root directory, run:
- docker-compose up

# 2. Set up data for text search
- Go to flaskr/utils/import_text_data.ipynb
- Run step by step to pull and insert data into Milvus

# 3. Test Text Search API
URL: http://localhost:5000/text
Query Param: text