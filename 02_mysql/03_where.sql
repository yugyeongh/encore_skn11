# where

-- 1) 비교 연산자
select menu_name, menu_price, orderable_status
	from tbl_menu
    where orderable_status = 'Y';

select menu_name, menu_price, orderable_status
	from tbl_menu
    where orderable_status <> 'Y';

select menu_name, menu_price, orderable_status
	from tbl_menu
    where orderable_status != 'Y';

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_price <= 10000
    order by menu_price desc;

-- 2) and
select menu_name, menu_price, orderable_status
	from tbl_menu
    where 10000 < menu_price and menu_price <= 20000
    order by menu_price desc;

-- 3) or
select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_price > 30000 or menu_name='열무김치라떼';

-- 4) between
select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_price between 10000 and 20000; -- from > where > select 순서

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_price not between 10000 and 20000;

-- 5) like
select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_name like '김치';

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_name like '%김치';

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_name like '김치%';

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_name like '%김치%';

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_name like '%김%치%';

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_name not like '%김치%';
    
-- 6) in
select menu_name, menu_price, orderable_status, category_code
	from tbl_menu
    where category_code=4
		or category_code=5
        or category_code=6;

select menu_name, menu_price, orderable_status, category_code
	from tbl_menu
    where category_code in (4,5,6);

select menu_name, menu_price, orderable_status, category_code
	from tbl_menu
    where category_code not in (4,5,6);

-- 7) is null
select category_code, category_name, ref_category_code
	from tbl_category
    where ref_category_code is null;

select category_code, category_name, ref_category_code
	from tbl_category
    where ref_category_code is not null;