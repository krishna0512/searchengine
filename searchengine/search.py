from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl import DocType, Index, fields
from elasticsearch.helpers import bulk
#from . import models
from searchengine.models import Book, Page

books = Index('books')
pages = Index('pages')

#connections.create_connection()  #create the connection of the search engine

@books.doc_type
class BookIndex(DocType):

	# pages = fields.NestedField(
	# 	properties={
	# 		'content':fields.TextField()
	# 	},
	# 	include_in_root=True
	# )
	class Meta:
		model=Book
		fields=['id','author','title']
		# related_models=[Page]

	# def get_instance_from_related(self,related_instance):
	# 	if isinstance(related_instance,Page):
	# 		return related_instance.book.all()

@pages.doc_type
class PageIndex(DocType):
	class Meta:
		model=Page
		fields=['id','content']

# #bulk indexer is been applied.
# def bulk_indexing():
#     BookIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing() for b in Book.objects.all().iterator()))

# def search(author):
# 	s = Search().filter('term', author_in=author)
# 	response = s.execute()
# 	return response