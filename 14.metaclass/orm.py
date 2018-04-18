#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Simple ORM using metaclass'

class Field(object):

    def __init__(self, name, column_type):
        print("==> Field.__init__")
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        print("==> StringField.__init__")
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        print("==> IntegerField.__init__")
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(clazz, name, bases, attrs):
        print("==> ModelMetaclass.__new__")
        if name=='Model':
            print("==> A new base model parent")
            return type.__new__(clazz, name, bases, attrs)

        print("==> A new model child")
        print('Found model: %s' % name)
        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(clazz, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        print("==> Model.__init__")
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        print("==> Model.__getattr__")
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        print("==> Model.__setattr__")
        self[key] = value

    def save(self):
        print("==> Model.save")
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

if __name__ == '__main__':

    print()
    print("Defined a User model class")
    class User(Model):
        id = IntegerField('id')
        name = StringField('username')
        email = StringField('email')
        password = StringField('password')

    print()
    print('#1 Instantiated a new instance')
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')

    print()
    print('#1 Trying to save user object')
    u.save()

    print()
    print('#2 Instantiated a new instance')
    u = User(id=12345, name='Michael', email='test@orm.org')

    print()
    print('#2 Trying to save user object')
    u.save()