user: admin, password: adminpwd

grant create session to admin;

grant create table to admin;

grant create tablespace to admin;

grant create view to admin;

alter user admin quota unlimited on ts_admin_main

create tablespace ts_admin_main
datafile '%ORACLE_HOME%\database\ts_admin_main.dbf' size 50M reuse
uniform size 128K

create table students(
sno varchar2(10) unique not null,
sname varchar2(20) not null,
sage number not null,
ssex varchar2(4) not null,
sid varchar2(18) unique not null,
sprofession varchar2(30) not null
);

create tablespace ts1 datafile '%ORACLE_HOME%\database\ts1.dbf' size 10M reuse;
create tablespace ts2 datafile '%ORACLE_HOME%\database\ts2.dbf' size 10M reuse;
create tablespace ts3 datafile '%ORACLE_HOME%\database\ts3.dbf' size 10M reuse;
create tablespace ts4 datafile '%ORACLE_HOME%\database\ts4.dbf' size 10M reuse;

create table student(
    sno varchar2(10) not null,
    sdept varchar2(30) not null,
    class varchar2(5) not null,
    sname varchar2(15) not null,
    ssex varchar2(4) not null,
    s_area varchar2(4) not null,
    CONSTRAINT student_sno_pk PRIMARY KEY (sno))
    ORGANIZATION INDEX
    INCLUDING sname 
    PCTTHRESHOLD 20
    STORAGE 
    (INITIAL  4K 
    NEXT  2K 
    PCTINCREASE 0 
    MINEXTENTS 1 
    MAXEXTENTS 1) 
    OVERFLOW  
    STORAGE 
    (INITIAL  4K 
    NEXT  2K 
    PCTINCREASE 0 
    MINEXTENTS 1 
    MAXEXTENTS 1);

insert into student
values('2004010525','ComputerScience','CS205','ZJ','male','west')

create table hash_card(
    card_id varchar2(6) not null,
    sno varchar2(10) not null,
    balance number(6,2) not null,
    constraint card_card_id_pk primary key(card_id),
    constraint card_sno_fk foreign key(sno) references student(sno))
    partition by hash(card_id)
    partitions 4
    store in (ts1,ts2,ts3,ts4);

alter table hash_card enable row movement;

insert into hash_card
values('000001','2004010525','1000')

create table terminal(
 	t_id varchar2(10) not null,
 	t_area varchar2(4) not null,
    t_name varchar2(15) not null,
    constraint terminal_t_id_pk primary key(t_id)
);

create table consume_record(
  	consume_id number(6) not null,
    card_id varchar2(6) not null,
    consume_money number(5,2) not null,
	consume_time date not null,
   	t_id varchar2(10) not null,
    constraint record_consume_id_pk primary key(consume_id),
    constraint record_t_id_fk foreign key(t_id) references terminal(t_id)
);

create table goods(
    goods_id varchar2(15) not null,
    goods_name varchar2(15) not null,
    goods_value number(6,2) not null,
    CONSTRAINT goods_id_pk PRIMARY KEY (goods_id))
    ORGANIZATION INDEX
    INCLUDING goods_name 
    PCTTHRESHOLD 20
    STORAGE  
    (INITIAL  4K 
    NEXT  2K 
    PCTINCREASE 0 
    MINEXTENTS 1 
    MAXEXTENTS 1) 
    OVERFLOW  
    STORAGE 
    (INITIAL  4K 
    NEXT  2K 
    PCTINCREASE 0 
    MINEXTENTS 1 
    MAXEXTENTS 1);

create table change_record(
    change_id varchar2(15) not null,
    sno varchar2(10) not null,
    change_type varchar2(10) not null,
    change_money number(10) not null,
    change_time date not null,
    constraint record_change_id_pk primary key(change_id),
    constraint record_sno_fk foreign key(sno) references student(sno)
);