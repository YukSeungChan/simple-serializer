Simple Serailizer
=================

Simple serialization for python model class.

Using Simple Serailizer
-----------------------
```python

  from simple_serializer import SerializerMixin


  class User(SerializerMixin):
      id = None
      name = None
  
      fields = ('id', 'name')
  
      def __init__(self, _id, name):
          self.id = _id
          self.name = name

  u = User(1, 'Loup')
  u.serialize()
```

Sample result
-------------

  {'id': 1, 'name': 'Loup'}


Author
------

Yuk SeungChan([@loup](http://loup.kr))
