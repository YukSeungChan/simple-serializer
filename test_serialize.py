# -*- coding:utf-8 -*-
import unittest

from simple_serializer import SerializerMixin


class User(SerializerMixin):
    id = None
    name = None

    fields = ('id', 'name')

    def __init__(self, _id, name):
        self.id = _id
        self.name = name


class Category(SerializerMixin):
    id = None
    name = None
    parent = None

    fields = ('id', 'name', 'parent')
    self_fields = ('id',)

    def __init__(self, _id, name, parent=None):
        self.id = _id
        self.name = name
        self.parent = parent


class Notice(SerializerMixin):
    id = None
    title = None
    content = None
    writer = None

    fields = ('id', 'title', 'content', 'writer')

    def __init__(self, _id, title, content, writer):
        self.id = _id
        self.title = title
        self.content = content
        self.writer = writer


class SerializeTest(unittest.TestCase):
    user = None
    notice = None
    parent_category = None
    category = None

    def setUp(self):
        self.user = User(1, 'Loup')
        self.notice = Notice(1, 'Test Notice', 'This is test notice.', self.user)
        self.parent_category = Category(1, 'Company')
        self.category = Category(2, 'Apple', self.parent_category)

    def test_user_serialize(self):
        result_dict = self.user.serialize()
        self.assertTrue('id' in result_dict)
        self.assertTrue('name' in result_dict)

    def test_notice_serialize(self):
        result_dict = self.notice.serialize()
        self.assertTrue('id' in result_dict)
        self.assertTrue('title' in result_dict)
        self.assertTrue('content' in result_dict)
        self.assertTrue('writer' in result_dict)

    def test_category_serialize(self):
        result_dict = self.parent_category.serialize()
        self.assertTrue('id' in result_dict)
        self.assertTrue('name' in result_dict)
        self.assertTrue('parent' in result_dict)
        self.assertEqual(result_dict['parent'], None)

    def test_category_fields_changed_serialize(self):
        tmp_parent_category = self.parent_category
        tmp_parent_category.fields = ('id', 'name')
        result_dict = tmp_parent_category.serialize()
        self.assertTrue('id' in result_dict)
        self.assertTrue('name' in result_dict)
        self.assertTrue('parent' not in result_dict)

    def test_self_referential_serialize(self):
        result_dict = self.category.serialize()
        self.assertTrue('id' in result_dict)
        self.assertTrue('name' in result_dict)
        self.assertTrue('parent' in result_dict)
        self.assertEquals(['id'], result_dict['parent'].keys())

    def test_self_referential_fields_changed_serialize(self):
        tmp_category = self.category
        tmp_category.self_fields = ('id', 'name')
        result_dict = tmp_category.serialize()
        self.assertTrue('id' in result_dict)
        self.assertTrue('name' in result_dict)
        self.assertTrue('parent' in result_dict)
        self.assertEquals(['id', 'name'], result_dict['parent'].keys())


if __name__ == '__main__':
    unittest.main()