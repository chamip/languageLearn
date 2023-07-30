### mysql必知必会

#### （第一章）了解sql
**数据库（database）** 保存有组织的数据的容器（通常是一个文件或一组文件）。

**数据库（database）** 保存有组织的数据的容器（通常是一个文件或一组文件）。

**模式（schema）** 关于数据库和表的布局及特性的信息。

**列（column）** 表中的一个字段。所有表都是由一个或多个列组成的。

**数据类型（datatype）** 所容许的数据的类型。每个表列都有相应的数据类型，它限制（或容许）该列中存储的数据。

**行（row）** 表中的一个记录。

**主键（primary key）** 一一列（或一组列），其值能够唯一区分表中每个行。

应该总是定义主键 虽然并不总是都需要主键，但大多数数据库设计人员都应保证他们创建的每个表具有一个主键，以便于以后的数据操纵和管理。

表中的任何列都可以作为主键，只要它满足以下条件：
- 任意两行都不具有相同的主键值；
- 每个行都必须具有一个主键值（主键列不允许NULL值）。

主键的最好习惯 除MySQL强制实施的规则外，应该坚持的几个普遍认可的最好习惯为：
- 不更新主键列中的值；
- 不重用主键列的值；
- 不在主键列中使用可能会更改的值。（例如，如果使用一个名字作为主键以标识某个供应商，当该供应商合并和更改其名字时，必须更改这个主键。）

SQL（发音为字母S-Q-L或sequel）是结构化查询语言（Structured Query Language）的缩写。SQL是一种专门用来与数据库通信的语言。

#### （第二章）mysql简介
MySQL是一种DBMS，即它是一种数据库软件。
DBMS可分为两类：一类为基于共享文件系统的DBMS，另一类为基于客户机—服务器的DBMS。前者（包括诸如Microsoft Access和FileMaker）用于桌面用途，通常不用于高端或更关键的应用。
MySQL、Oracle以及Microsoft SQL Server等数据库是基于客户机—服务器的数据库。客户机—服务器应用分为两个不同的部分。服务器部分是负责所有数据访问和处理的一个软件。这个软件运行在称为数据库服务器的计算机上。

#### （第三章）使用mysql
为了连接到MySQL，需要以下信息：
- 主机名（计算机名）——如果连接到本地MySQL服务器，为localhost；
- 端口（如果使用默认端口3306之外的端口）；
- 一个合法的用户名；
- 用户口令（如果需要）。
```mysql
mysql -u ben -p -h myserver -P 3306
```

在你最初连接到MySQL时，没有任何数据库打开供你使用。在你能执行任意数据库操作前，需要选择一个数据库。为此，可使用USE关键字。关键字(key word) 作为MySQL语言组成部分的一个保留字。决不要用关键字命名一个表或列。
```mysql
USE mydb;
```

显示可用的数据库：
```mysql
SHOW DATABASES;
```

显示数据库内的可用的表：
```mysql
SHOW TABLES;
```

显示表列：
```mysql
SHOW COLUMNS FROM mydb;
```

- SHOW STATUS，用于显示广泛的服务器状态信息；
- SHOW CREATE DATABASE和SHOW CREATE TABLE，分别用来显示创
建特定数据库或表的MySQL语句；
- SHOW GRANTS，用来显示授予用户（所有用户或特定用户）的安
全权限；
- SHOW ERRORS和SHOW WARNINGS，用来显示服务器错误或警告消息。

```mysql
HELP SHOW;
```

#### （第四章）检索数据
###### 检索不同的行
就是当检索某列时，去掉重复的要用DISTINCT。
不能部分使用DISTINCT DISTINCT关键字应用于所有列而不仅是前置它的列。
比如说检索表的某两列，如果某两行的这两列数据完全一样，就会过滤掉其中一行。
<img width="1356" alt="1" src="https://github.com/chamip/languageLearn/assets/42117528/ad881e1b-2af7-4ec6-b801-11bc69eafb76">
<img width="742" alt="2" src="https://github.com/chamip/languageLearn/assets/42117528/20a1d8c5-3629-40a2-9e1e-befa714bcc70">

###### 限制结果
为了返回第一行或前几行，可使用LIMIT子句。
为得出下一个5行，可指定要检索的开始行和行数。第一个数为开始位置，第二个数为要检索的行数。
<img width="711" alt="3" src="https://github.com/chamip/languageLearn/assets/42117528/f06976f0-10b3-441d-815e-6328e556a135">

###### 使用完全限定的表名
就是对列增加表名限定，或对表增加数据库名限定；
