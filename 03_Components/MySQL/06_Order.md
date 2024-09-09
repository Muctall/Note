- [Base Categories](#base-categories)
  - [DDL (Data Definition Language)](#ddl-data-definition-language)
  - [DQL (Data Query Language)](#dql-data-query-language)
  - [DML(Data Manipulation Language)](#dmldata-manipulation-language)
  - [DCL (Data Control Language)](#dcl-data-control-language)
  - [TCL (Transaction Control Language)](#tcl-transaction-control-language)
- [查询](#查询)
  - [基础语法](#基础语法)
  - [基本查询](#基本查询)
    - [SELECT语句的执行顺序](#select语句的执行顺序)
    - [DISTINCT](#distinct)
    - [LIMIT](#limit)
    - [ORDER BY](#order-by)
    - [GROUP BY/HAVING](#group-byhaving)
    - [操作符](#操作符)
  - [常用函数](#常用函数)
    - [汇总](#汇总)
    - [String](#string)
    - [Time](#time)
    - [Math](#math)
  - [子查询](#子查询)
    - [INNER JOIN](#inner-join)
    - [OUTER JOIN](#outer-join)
  - [UNION](#union)
- [视图(View)](#视图view)
- [存储过程(procedure)](#存储过程procedure)
- [游标(cursor)](#游标cursor)
- [触发器(TRIGGER)](#触发器trigger)
- [transaction](#transaction)
- [权限管理](#权限管理)

![](source/SQLCommendCategories.png)

# Base Categories
## DDL (Data Definition Language)
DDL can be used to define the database schema. It simply deals with descriptions of the database schema and is used to create and modify the structure of database objects in the database. DDL is a set of SQL commands used to create, modify, and delete database structures but not data. These commands are normally not used by a general user, who should be accessing the database via an application.

    DDL commands: 

    CREATE: This command is used to create the database or its objects (like table, index, function, views, store procedure, and triggers).

    DROP: This command is used to delete objects from the database.

    ALTER: This is used to alter the structure of the database.

    TRUNCATE: This is used to remove all records from a table, including all spaces allocated for the records are removed.

    COMMENT: This is used to add comments to the data dictionary.

    RENAME: This is used to rename an object existing in the database.


## DQL (Data Query Language)
DQL statements are used for performing queries on the data within schema objects. 

    SELECT: It is used to retrieve data from the database.

## DML(Data Manipulation Language)
The SQL commands that deal with the manipulation of data present in the database belong to DML or Data Manipulation Language and this includes most of the SQL statements. It is the component of the SQL statement that controls access to data and to the database. Basically, DCL statements are grouped with DML statements.

    INSERT: It is used to insert data into a table.

    UPDATE: It is used to update existing data within a table.

    DELETE: It is used to delete records from a database table.

    LOCK: Table control concurrency.

    CALL: Call a PL/SQL or JAVA subprogram.

    EXPLAIN PLAN: It describes the access path to data.

## DCL (Data Control Language)
DCL includes commands such as GRANT and REVOKE which mainly deal with the rights, permissions, and other controls of the database system. 


    GRANT: This command gives users access privileges to the database.

        Syntax:
        GRANT SELECT, UPDATE ON MY_TABLE TO SOME_USER, ANOTHER_USER;  

    REVOKE: This command withdraws the user’s access privileges given by using the GRANT command.

        Syntax:
        REVOKE SELECT, UPDATE ON MY_TABLE FROM USER1, USER2;  


## TCL (Transaction Control Language)
Transactions group a set of tasks into a single execution unit. Each transaction begins with a specific task and ends when all the tasks in the group successfully complete. If any of the tasks fail, the transaction fails. Therefore, a transaction has only two results: success or failure. You can explore more about transactions here. Hence, the following TCL commands are used to control the execution of a transaction: 

    BEGIN: Opens a Transaction.

    COMMIT: Commits a Transaction.

        Syntax:
        COMMIT;  

    ROLLBACK: Rollbacks a transaction in case of any error occurs.

        Syntax:
        ROLLBACK;  

    SAVEPOINT: Sets a save point within a transaction.

        Syntax:
        SAVEPOINT SAVEPOINT_NAME;  

# 查询
## 基础语法

```SQL
    CREATE DATABASE test;
    USE test;
    # 创建表
    CREATE TABLE mytable (
    id INT NOT NULL AUTO_INCREMENT,
    col1 INT NOT NULL DEFAULT 1,
    col2 VARCHAR(45) NULL,
    col3 DATE NULL,
    PRIMARY KEY (`id`));
    # 修改表添加列
    ALTER TABLE mytable
    ADD col CHAR(20);
    # 修改列和属性
    ---ALTER TABLE 表名 CHANGE 原字段名 新字段名 字段类型 约束条件
    ALTER TABLE mytable 
    CHANGE col col1 CHAR(32) NOT NULL DEFAULT '123';
    # 删除列
    ALTER TABLE mytable
    DROP COLUMN col;
    # 删除表
    DROP TABLE mytable;
    # 插入普通插入
    INSERT INTO mytable(col1, col2)
    VALUES(val1, val2);
    # 插入检索出来的数据
    INSERT INTO mytable1(col1, col2)
    SELECT col1, col2
    FROM mytable2;
    将一个表的内容插入到一个新表
    CREATE TABLE newtable AS
    SELECT * FROM mytable;
    # 更新
    UPDATE mytable
    SET col = val
    WHERE id = 1;
    # 删除
    DELETE FROM mytable
    WHERE id = 1;
```
DISTINCT相同值只会出现一次。它作用于所有列，也就是说所有列的值都相同才算相同。SELECT  col1, DISTINCT col2
FROM mytable;

## 基本查询

### SELECT语句的执行顺序
SELECT语句的执行顺序通常按照以下顺序进行：

FROM: 从指定的表中选择数据。
JOIN: 如果在FROM子句中有多个表，进行表连接操作。
WHERE: 对表中的数据进行条件筛选。
GROUP BY: 根据指定的列对结果集进行分组。
HAVING: 对分组后的数据进行条件筛选。
SELECT: 选择要检索的列。
DISTINCT: 去除重复的行。
ORDER BY: 对结果集进行排序。
LIMIT/OFFSET: 限制结果集的数量和偏移。

### DISTINCT
`SELECT DISTINCT` 而不是 `DISTINCT`。DISTINCT 关键字用于删除结果集中的重复行，而在 SELECT 语句中，应该指定哪些列需要考虑去重。
```SQL
SELECT DISTINCT col1, col2
FROM mytable;
```
这样会选择唯一的 (col1, col2) 组合。如果你只想选择 col1 的唯一值，可以这样写：
```SQL
SELECT DISTINCT col1
FROM mytable;
```

### LIMIT
限制返回的行数。可以有两个参数，第一个参数为起始行，从 0 开始；第二个参数为返回的总行数。
```SQL
# 返回前 5 行
SELECT *
FROM mytable
LIMIT 5;
# 返回前 5 行
SELECT *
FROM mytable
LIMIT 0, 5;
# 返回第 3 ~ 5 行
SELECT *
FROM mytable
LIMIT 2, 3;
```
### ORDER BY
排序默认升序ASC，降序DESC。可以按多个列进行排序，并且为每个列指定不同的排序方式。
```SQL
SELECT *
FROM mytable
ORDER BY col1 DESC, col2 ASC;
```
### GROUP BY/HAVING
分组就是把具有相同的数据值的行放在同一组中。
可以对同一分组数据使用汇总函数进行处理，例如求分组数据的平均值等。
指定的分组字段除了能按该字段进行分组，也会自动按该字段进行排序。
### 操作符
| 运算符 | 描述 | 备注 |
| --- | --- | --- |
| `<>`  `!=` | 不等于 |
| `<=`  `!<` | 小于等于 |
| `>=`  `!>` | 大于等于 |
| `BETWEEN` | 在两个值之间 |
| `IS NULL`  `IS NOT NULL` | 为/不为 NULL 值 | NULL 与 0、空字符串都不同 |
| `AND` | 逻辑 AND 运算符 | AND 和 OR 用于连接多个过滤条件。优先处理 AND|
| `OR` | 逻辑 OR 运算符 |
| `()` | 用于改变运算符的优先级 |
| `IN` | 匹配一组值 | IN 操作符用于匹配一组值，其后也可以接一个 SELECT 子句，从而匹配子查询得到的一组值 |
| `NOT` | 否定一个条件 |

## 常用函数
`CONCAT()` 
用于连接两个字段。

`TRIM()`
去除首尾空格。

```SQL
SELECT CONCAT(TRIM(col1), '(', TRIM(col2), ')') AS concat_col
FROM mytable;
```
### 汇总
| 函数   | 描述               |
|--------|--------------------|
| AVG()  | 返回某列的平均值    |
| COUNT()| 返回某列的行数      |
| MAX()  | 返回某列的最大值    |
| MIN()  | 返回某列的最小值    |
| SUM()  | 返回某列值之和      |
### String
| 函数      | 描述                   |
|-----------|------------------------|
| LEFT()    | 返回左边的字符         |
| RIGHT()   | 返回右边的字符         |
| LOWER()   | 转换为小写字符         |
| UPPER()   | 转换为大写字符         |
| LTRIM()   | 去除左边的空格         |
| RTRIM()   | 去除右边的空格         |
| LENGTH()  | 返回字符串长度         |
| SOUNDEX() | 转换为语音值           |
### Time
日期格式: YYYY-MM-DD
时间格式: HH:MM:SS
| 函数           | 描述                           |
|----------------|--------------------------------|
| AddDate()      | 增加一个日期（天、周等）        |
| AddTime()      | 增加一个时间（时、分等）        |
| CurDate()      | 返回当前日期                   |
| CurTime()      | 返回当前时间                   |
| Date()         | 返回日期时间的日期部分          |
| DateDiff()     | 计算两个日期之差               |
| Date_Add()     | 高度灵活的日期运算函数         |
| Date_Format()  | 返回一个格式化的日期或时间串    |
| Day()          | 返回一个日期的天数部分          |
| DayOfWeek()    | 对于一个日期，返回对应的星期几  |
| Hour()         | 返回一个时间的小时部分          |
| Minute()       | 返回一个时间的分钟部分          |
| Month()        | 返回一个日期的月份部分          |
| Now()          | 返回当前日期和时间              |
| Second()       | 返回一个时间的秒部分            |
| Time()         | 返回一个日期时间的时间部分      |
| Year()         | 返回一个日期的年份部分          |
### Math
| 函数   | 说明     |
|--------|----------|
| SIN()  | 正弦     |
| COS()  | 余弦     |
| TAN()  | 正切     |
| ABS()  | 绝对值   |
| SQRT() | 平方根   |
| MOD()  | 余数     |
| EXP()  | 指数     |
| PI()   | 圆周率   |
| RAND() | 随机数   |

## 子查询

### INNER JOIN
`INNER JOIN` `JOIN`
```SQL
SELECT A.value, B.value
FROM tablea AS A INNER JOIN tableb AS B
ON A.key = B.key;
#隐式
SELECT A.value, B.value
FROM tablea AS A, tableb AS B
WHERE A.key = B.key;
```
### OUTER JOIN
分为左外连接，右外连接以及全外连接。
`LEFT OUTER JOIN` `RIGHT OUTER JOIN` `FULL OUTER JOIN`
```SQL
SELECT Customers.cust_id, Orders.order_num
FROM Customers LEFT OUTER JOIN Orders
ON Customers.cust_id = Orders.cust_id;
```

## UNION 
使用 UNION 来组合两个查询，如果第一个查询返回 M 行，第二个查询返回 N 行，那么组合查询的结果一般为 M+N 行。每个查询必须包含相同的列、表达式和聚集函数。默认会去除相同行，如果需要保留相同行，使用 UNION ALL。只能包含一个 ORDER BY 子句，并且必须位于语句的最后。

# 视图(View)
视图是虚拟的表，本身不包含数据，也就不能对其进行索引操作。对视图的操作和对普通表的操作一样。视图具有如下好处:简化复杂的 SQL 操作，比如复杂的连接；只使用实际表的一部分数据；通过只给用户访问视图的权限，保证数据的安全性；更改数据格式和表示。
```SQL
CREATE VIEW myview AS
SELECT Concat(col1, col2) AS concat_col, col3*col4 AS compute_col
FROM mytable
WHERE col5 = val;
```

# 存储过程(procedure)
存储过程可以看成是对一系列 SQL 操作的批处理。使用存储过程的好处:代码封装，保证了一定的安全性；代码复用；由于是预先编译，因此具有很高的性能。命令行中创建存储过程需要自定义分隔符，因为命令行是以 ; 为结束符，而存储过程中也包含了分号，因此会错误把这部分分号当成是结束符，造成语法错误。包含 in、out 和 inout 三种参数。给变量赋值都需要用 select into 语句。每次只能给一个变量赋值，不支持集合的操作。
```SQL
delimiter //

create procedure myprocedure( out ret int )
    begin
        declare y int;
        select sum(col1)
        from mytable
        into y;
        select y*y into ret;
    end //

delimiter ;
call myprocedure(@ret);
select @ret;
```


# 游标(cursor)
在存储过程中使用游标可以对一个结果集进行移动遍历。游标主要用于交互式应用，其中用户需要对数据集中的任意行进行浏览和修改。使用游标的四个步骤:声明游标，这个过程没有实际检索出数据；打开游标；取出数据；关闭游标；
```SQL
delimiter //
create procedure myprocedure(out ret int)
    begin
        declare done boolean default 0;

        declare mycursor cursor for
        select col1 from mytable;
        # 定义了一个 continue handler，当 sqlstate '02000' 这个条件出现时，会执行 set done = 1
        declare continue handler for sqlstate '02000' set done = 1;

        open mycursor;

        repeat
            fetch mycursor into ret;
            select ret;
        until done end repeat;

        close mycursor;
    end //
 delimiter ;
```

# 触发器(TRIGGER)
触发器会在某个表执行以下语句时而自动执行: DELETE、INSERT、UPDATE。触发器必须指定在语句执行之前还是之后自动执行，之前执行使用 BEFORE 关键字，之后执行使用 AFTER 关键字。BEFORE 用于数据验证和净化，AFTER 用于审计跟踪，将修改记录到另外一张表中。

INSERT 触发器包含一个名为 NEW 的虚拟表。
```SQL
CREATE TRIGGER mytrigger AFTER INSERT ON mytable
FOR EACH ROW SELECT NEW.col into @result;

SELECT @result; -- 获取结果
```
DELETE 触发器包含一个名为 OLD 的虚拟表，并且是只读的。
UPDATE 触发器包含一个名为 NEW 和一个名为 OLD 的虚拟表，其中 NEW 是可以被修改的，而 OLD 是只读的。
MySQL 不允许在触发器中使用 CALL 语句，也就是不能调用存储过程。

# transaction
保留点(savepoint)不能回退 CREATE 和 DROP 语句。
MySQL 的事务提交默认是隐式提交，每执行一条语句就把这条语句当成一个事务然后进行提交。当出现 START TRANSACTION 语句时，会关闭隐式提交；
当 COMMIT 或 ROLLBACK 语句执行后，事务会自动关闭，重新恢复隐式提交。
通过设置 autocommit 为 0 可以取消自动提交；autocommit 标记是针对每个连接而不是针对服务器的。如果没有设置保留点，ROLLBACK 会回退到 START TRANSACTION 语句处；
如果设置了保留点，并且在 ROLLBACK 中指定该保留点，则会回退到该保留点。
```SQL
START TRANSACTION
// ...
SAVEPOINT delete1
// ...
ROLLBACK TO delete1
// ...
COMMIT
```

# 权限管理
MySQL 的账户信息保存在 mysql 这个数据库中。
```SQL
USE mysql;
SELECT user FROM user;
```
创建账户新创建的账户没有任何权限。
```SQL
CREATE USER myuser IDENTIFIED BY 'mypassword';
```
修改账户名
```SQL
RENAME myuser TO newuser;
```
删除账户
```SQL
DROP USER myuser;
```
查看权限
```SQL
SHOW GRANTS FOR myuser;
```
授予权限账户用 username@host 的形式定义，username@% 使用的是默认主机名。
```SQL
GRANT SELECT, INSERT ON mydatabase.* TO myuser;
```
删除权限
GRANT 和 REVOKE 可在几个层次上控制访问权限:整个服务器，使用 GRANT ALL 和 REVOKE ALL；整个数据库，使用 ON database.*；特定的表，使用 ON database.table；特定的列；特定的存储过程。
```SQL
REVOKE SELECT, INSERT ON mydatabase.* FROM myuser;
```
更改密码必须使用 Password() 函数
```SQL
SET PASSWROD FOR myuser = Password('new_password');
```
