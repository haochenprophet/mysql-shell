import mysqlx
session=mysqlx.getNodeSession('root:guidev!@localhost:33060')
schema = session.getSchema('sakila')
session.sql('drop table if exists sakila.friends;').execute()
session.sql('create table sakila.friends (name varchar(50), last_name varchar(50), age integer, gender varchar(20));').execute()
table = session.sakila.friends
table.insert('name','last_name','age','gender').values('jack','black', 17, 'male')
table.insert('name','last_name','age','gender').values('adam', 'sandler', 15, 'male')
table.insert('name','last_name','age','gender').values('brian', 'adams', 14, 'male')
table.insert('name','last_name','age','gender').values('alma', 'lopez', 13, 'female')
table.insert('name','last_name','age','gender').values('carol', 'shiffield', 14, 'female')
table.insert('name','last_name','age','gender').values('donna', 'summers', 16, 'female')
table.insert('name','last_name','age','gender').values('angel', 'down', 14, 'male').execute()
result = table.update().set('age', 14).orderBy(['age']).limit(1).execute()
result2 = table.update().set('last_name','downey').set('age',15).where('name="angel"').execute()
result3 = table.update().set('last_name','downey').set('age',15).where('name=:name').bind('name', 'angel').execute()
result4 = table.select().where("age < 40").orderBy(['name']).limit(3).execute()
result4
