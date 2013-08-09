import mysql.connector
import codecs
class MySQLCursorDict(mysql.connector.cursor.MySQLCursor):
	def _row_to_python(self, rowdata, desc=None):
		row = super(MySQLCursorDict, self)._row_to_python(rowdata, desc)
		if row:
			return dict(zip(self.column_names, row))
		return None

class class_mysql:
	def __init__(self):
		self.app = "mysql"
		self.cnx = None
		self.Conn = None
	def connector(self,_host,_user,_passwd,_db,_char):
		self.cnx = mysql.connector.connect(user=_user, password=_passwd, host=_host, database=_db,charset=_char)
		self.Conn = self.cnx.cursor(cursor_class=MySQLCursorDict)
#.Conn.execute(select_sql)
	def saveDB(self , _db_name ,_dir ):
		mLogFile = codecs.open("DB_log.txt", "w", "utf-8")

		_mData = self.InsertSql(_db_name ,_dir)
		_data = tuple( _mData['val'] ) 
		_sql = _mData['sql']
		mLogFile.write( _sql + "\n" )
		try:
			self.Conn.execute( _sql , _data ) 
		except mysql.connector.Error as err:
			mLogFile.write( u"sql: " + _sql + "\n" )
			mLogFile.write( u"\n" )
			for _vs in _data:
				mLogFile.write( u" , %s " % (_vs) )
			msg = '[ErrorMsg] '
			print msg
			# mLogFile.write( u"\n" )
			# error_text = err.args[1]
			# error_text = error_text.replace('\ufffd', '_')
			# msg = "Error: %s (%s)" % (err.args[0], error_text)
			# mLogFile.write( str(msg).decode('big5', 'replace') )
			print msg

		#_data
		# self.Conn.commit()
		# print _re_msg
		return 

	def getDescribe(self , _table_name ):
		_sql = "DESCRIBE " + _table_name #mysql get DESCRIBE
		self.Conn.execute( _sql )
		rows = self.Conn.fetchall()
		return rows

	def InsertSql(self , _table_name , _dir ):
		_baseTables = []
		_userTables = {}

		_sql_headerVal = []
		_sql_insertVal = []
		_sql_insertValKey = []
		_rows = self.getDescribe( _table_name )
		for _row in _rows:
			# _baseTables.append(_row.COLUMN_NAME)
			_baseTables.append(_row['Field'])
		for _val in _baseTables:
			if (_val in _dir ) == 1:
				_userTables[_val] = _dir[_val]

		for _val in _userTables.keys():
			_sql_headerVal.append(_val)
			_sql_insertValKey.append("%s")
			_sql_insertVal.append( _userTables[_val] )

		_insert_header_str = ','.join( _sql_headerVal )
		_insert_values_str = ','.join( _sql_insertValKey ) 
		_sql = " INSERT INTO "+_table_name+"(" + _insert_header_str + " ) VALUES( " + _insert_values_str + ") "
		_mlist = {}
		_mlist['sql'] = _sql
		_mlist['val'] = _sql_insertVal
		return  _mlist 




def init():
	return 0