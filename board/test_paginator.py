from django.core.paginator import Paginator

objects = ['john', 'paul', 'george', 'ringo', 'jane', 'mag']

page = Paginator(objects, 2)
print(type(page))
