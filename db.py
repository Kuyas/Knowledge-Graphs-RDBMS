import pymysql
import re
from prettytable import PrettyTable
import warnings
warnings.filterwarnings("ignore")
	
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='dbs',
)

def addEntity(entity1,entity2,relation):
	entity1 = entity1.lower()
	entity2 = entity2.lower()
	relation = relation.lower()

	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO entities values (%s);"
			try:
				if(not searchinEnt(entity1)):
					cursor.execute(sql,(entity1))
				if(not searchinEnt(entity2)):
					cursor.execute(sql,(entity2))
					# cursor.execute(sql,(entity1))
				print("Entity Added")
			except Exception as e:
				print(entity1+" already exists")
			try:
				# cursor.execute(sql,(entity2))
				print("Entity Added")
			except Exception as e:
				print(entity2 +" already exists")
		connection.commit()
	finally:
		pass

	try:
		with connection.cursor() as cursor:
			sql = "CREATE TABLE IF NOT EXISTS `%s` ( `entity1` VARCHAR(50) NOT NULL , `entity2` VARCHAR(50) NOT NULL, PRIMARY KEY (`entity1`, `entity2`),FOREIGN KEY (entity1) REFERENCES entities(name),FOREIGN KEY (entity2) REFERENCES entities(name)) ENGINE = InnoDB;"%(relation)
			try:
				cursor.execute(sql)
				# sql = "INSERT INTO `%s` values (%s,%s);"
				sql = ("INSERT INTO {table} (entity1, entity2) VALUES (%s,%s)")
				table_name = relation
				data_word = (entity1, entity2)
				try:
					# print(sql.format(table=table_name),data_word)
					cursor.execute(sql.format(table=table_name),data_word)
					connection.commit()
					print("New relation Created")
				except:
					print("Failed")
			except Exception as e:
				print("Table Failed")
	finally:
		pass

def readEntity():

	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM `dbs`"
			try:
				cursor.execute(sql)
				result = cursor.fetchall()
				print(result)
				print("Enitity Name")
				print("---------------------------------------------------------------------------")
				for row in result:
					print(str(row[0]),row[1],row[2])
			except:
				print("Oops! Something wrong")
		connection.commit()
	finally:
		pass

def deleteEntity(entity1,entity2,relation):
	entity1 = entity1.lower()
	entity2 = entity2.lower()
	relation = relation.lower()
	try:
		with connection.cursor() as cursor:
			sql = "DELETE from `%s` where entity1='%s' and entity2='%s';"%(relation,entity1,entity2)
			try:
				print(sql)
				cursor.execute(sql)
				connection.commit()
				print("deleted")
			except Exception as e:
				print("failed to delete")
	finally:
		pass

def readdbEntity():
	try:
		with connection.cursor() as cursor:
			sql = "SELECT table_name FROM information_schema.tables WHERE table_schema ='dbs';"
			try:
				cursor.execute(sql)
				result = cursor.fetchall()
				# print(result)
				# t1 = PrettyTable(['All'])
				ans = ''
				# data = ''
				for table in result:
					word1 = str(table)
					word ="".join(re.split("[^a-zA-Z0-9]*", word1))
					# print(word)
					if word == 'entities':
						print(word)
						ans+='\t'+word.upper()+'\n'
						sql = "SELECT * from `%s`;"%(table)
						# print(sql)
						cursor.execute(sql)
						row = cursor.fetchall()
						t = PrettyTable(['Entity Name'])
						for index in row:
							t.add_row([index[0]])
							ans+=index[0]+'\n'
							# print(index[0])

						print(t)
						ans+='\n'
						# data+=t.get_string()+'\n'
						print("\n")
						continue
					print("Relation: " + word)
					sql = "SELECT * from `%s`;"%(table)
					# print(sql)
					cursor.execute(sql)
					row = cursor.fetchall()
					# print(row)
					ans+='\t'+word.upper()+'\n'
					t = PrettyTable(['Entity1', 'Entity2'])
					# print("Enitity Name\t\tEntity Name")
					# print("---------------------------------------------------------------------------")
					for index in row:
						t.add_row([index[0],index[1]])
						ans+=index[0]+'\t\t'+index[1]+'\n'
						# print(t)
						# print(index[0]+"\t\t"+index[1])
						# print("---------------------------------------------------------------------------")
					print(t)
					ans+='\n'
					# data+= t.get_string()+'\n'
					print("\n")
			except:
				print("Oops! Something wrong")
		connection.commit()
	finally:
		# ans=t.get_string()
		return ans

def search(entity1,entity2):
	entity1 = entity1.lower()
	entity2 = entity2.lower()
	try:
		empty_flag = 1
		with connection.cursor() as cursor:
			sql = "SELECT table_name FROM information_schema.tables WHERE table_schema ='dbs';"
			try:
				cursor.execute(sql)
				result = cursor.fetchall()
				# print(result)

				for table in result:
					word1 = str(table)
					word ="".join(re.split("[^a-zA-Z0-9]*", word1))
					# print(word)
					if word == 'entities':
						continue
					# print("Relation: " + word)
					sql = "SELECT * from `%s` WHERE entity1='%s' and entity2='%s';"%(word,entity1,entity2)
					sql1 = "SELECT * from `%s` WHERE entity1='%s' and entity2='%s';"%(word,entity2,entity1)
					# print(sql)
					cursor.execute(sql)
					row = cursor.rowcount
					if row is not 0:
						empty_flag = 0
						break

					cursor.execute(sql1)
					row = cursor.rowcount
					if row is not 0:
						empty_flag = 0
						break

			except:
				print("Oops! Something wrong")
		connection.commit()
	finally:
		return empty_flag

def searchinEnt(entity1):
	with connection.cursor() as cursor:
		sql = "CALL search('%s')"%(entity1)
		cursor.execute(sql)
		flag = cursor.fetchall()
		flag = "".join(re.split("[^a-zA-Z0-9]*", str(flag)))
		if(int(flag) > 0):
			print(entity1 + " exists")
			return 1
	return 0

if __name__ == '__main__':
	# deleteEntity("ssk","shreyas",'r1')
	# readdbEntity()
	searchinEnt('pancake')
	# print(search('shreyas','ssk'))
	connection.close()