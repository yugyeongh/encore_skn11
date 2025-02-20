# dml

select * from tbl_menu;

# insert
-- insert into 테이블명 values (컬럼 순으로, 삽입할, 데이터, 나열, ...)
insert into tbl_menu values (null, '곰탕', 9500, 6, 'Y'); -- 컬럼 순을 알고 있다는 전제

insert into tbl_menu(menu_code, menu_name, menu_price, orderable_status, category_code)
	values (null, '차돌짬뽕', 15000, 'Y', 6);

insert into tbl_menu(menu_name, menu_price, category_code, orderable_staus)
	values('만잔라떼',4500,7,'Y');

-- multi insert
insert into tbl_menu
	values
		(null, '유자민트티', 6900, 12, 'Y'),
        (null, '프렌치프라이', 7500, 7, 'Y'),
        (null, '훈제오리샐러드', 9500, 7 ,'Y');

-- insert into tbl_menu values (100, '1번 음식', 100, 10, 'Y');

# update
-- update 테이블명
--   set 컬럼명1 = 수정할 데이터,
--       컬럼명2 = 수정할 데이터,
--       ...
-- [ where 수정 대상 데이터 조건 ];

update tbl_menu
	set menu_name = '100번이었던 음식', menu_price = 19000
    where menu_code = 100; -- safe update 모드가 설정되어 있으면 where 절 없이 수정이 불가함
    
# delete
-- delete from 테이블명 [ where 삭제 조건];
delete from tbl_menu
	where menu_code = 101;
    
delete from tbl_menu
	order by menu_code desc
    limit 3;

# replace
-- replace는 중복값에 대해서는 데이터를 덮어쓰고, 중복값이 없다면 insert함
-- into 키워드는 생략이 가능
replace into tbl_menu values (100, '100번 음식 replace!!', 100, 10, 'Y');
replace tbl_menu values(120,'없는 메뉴 replace',1111,8,'Y'); -- 기존에 없는 row에 대해 replace를 하면 insert와 같은 동작을 함


select * from tbl_menu;




