import numpy as np
from towhee import pipe, ops

# Search one text in Milvus
search_pipe = (pipe.input('query')
                    .map('query', 'vec', ops.text_embedding.dpr(model_name="facebook/dpr-ctx_encoder-single-nq-base"))
                    .map('vec', 'vec', lambda x: x / np.linalg.norm(x, axis=0))
                    .flat_map('vec', ('id', 'score', 'title'), ops.ann_search.milvus_client(host='127.0.0.1', 
                                                                                   port='19530',
                                                                                   collection_name='search_article_in_medium',
                                                                                   output_fields=['title']))  
                    .output('query', 'id', 'score', 'title')
               )


# Search text with some expr
search_pipe__with_expression = (pipe.input('query')
                    .map('query', 'vec', ops.text_embedding.dpr(model_name="facebook/dpr-ctx_encoder-single-nq-base"))
                    .map('vec', 'vec', lambda x: x / np.linalg.norm(x, axis=0))
                    .flat_map('vec', ('id', 'score', 'title', 'link', 'reading_time', 'publication', 'claps', 'responses'), 
                                       ops.ann_search.milvus_client(host='127.0.0.1', 
                                                                    port='19530',
                                                                    collection_name='search_article_in_medium',
                                                                    expr='title like "Python%"',
                                                                    output_fields=['title', 'link', 'reading_time', 'publication', 'claps', 'responses'], 
                                                                    limit=5))  
                    .output('query', 'id', 'score', 'title', 'link', 'reading_time', 'publication', 'claps', 'responses')
               )