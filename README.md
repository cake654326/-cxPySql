## cxPyMysql Object ##

**cxPyMysql** 建立在 mysql.connector 之下的物件

### 提供功能 ###

1. **鏈接**
	1. connector(_host,_user,_passwd,_db,_char)
	2. **cxPyMysql.Conn** 為 cursor
2. **getDescribe**
	1. getDescribe( _table_name )
		1. @_table_name 資料表名稱
	2. 回傳 資料表欄位資訊
3. **InsertSql**
	- InsertSql( _table_name , _dir )
		- 建立 insertSql 語法
		- @_table_name 資料表名稱
		- @_dir 輸入欄位所需資料
			- _dir['name'] = 'jeff'
			- _dir['id'] = 10
		- @return [結構]
			- _return['sql'] insert sql 包含 %s  
			- _return['val'] 資料串列
4. **saveDB**
	- 自動進行insertSql
	- P.S. 此版本尚未建立 autoSave(insert or update)自動判斷功能
	- saveDB( _db_name ,_dir ) 同 InsertSql
		- 自動建立 DB_log.txt
		-  執行 self.Conn.execute( _sql , _data ) 功能

### 範例 ###
	user = 'root'
	pwd  = 'seat'
	host = '127.0.0.1'
	db   = 'test_tp'
	
	#鏈接資料庫
	mysqlObj = mSqlControl.class_mysql()
	mysqlObj.connector(host,user,pwd,db,"utf8")
	
	#設定資料
	_insertData = {}
	_insertData['name'] = u"中文_python_user1"
	_insertData['id'] = "0008"
	_insertData['PaswdCode'] = "999991"

	#顯示建立SQL資料 （非必要）
	print mysqlObj.InsertSql( u"sign_up_data", _insertData)

	#Insert
	mysqlObj.saveDB( u"sign_up_data", _insertData)