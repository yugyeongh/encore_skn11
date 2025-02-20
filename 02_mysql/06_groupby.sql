# group by

select category_code
	from tbl_menu
    group by category_code;

select category_code, count(category_code)
	from tbl_menu
    group by category_code;

select category_code, count(*)
	from tbl_menu
    group by category_code;
    
select category_code, sum(menu_price)
	from tbl_menu
    group by category_code;

select category_code, avg(menu_price)
	from tbl_menu
    group by category_code;

select category_code, menu_price, count(*)
	from tbl_menu
    group by category_code, menu_price
    order by category_code, menu_price;


# having -- groupby에 조건을 붙이기 위해 씀
select category_code, count(*)
	from tbl_menu
    group by category_code
    having category_code between 5 and 8;

# rollup
-- 컬럼 한 개를 이용해 groupby 후 rollup -> 총계(합계)
select category_code, sum(menu_price)
	from tbl_menu
    group by category_code
    with rollup;

-- 컬럼 두 개를 활용해 groupby 후 rollup -> 중간 합계 + 총계
-- 먼저 나온 컬럼의 총합을 구하고, 이후에 나오는 컬럼의 총합까지 구하는 방식
select category_code, menu_price, count(menu_price)
	from tbl_menu
    group by category_code, menu_price
    with rollup;
