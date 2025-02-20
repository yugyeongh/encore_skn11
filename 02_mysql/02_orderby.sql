# order by - 무조건 가장 끝에 온다!

select menu_code, menu_name, menu_price from tbl_menu
    order by menu_name desc; -- default는 asc
    
select menu_code, menu_name, menu_price from tbl_menu
    order by menu_price, menu_name;
    
select menu_code, menu_name, menu_price from tbl_menu
    order by menu_code * menu_price;

select menu_code, menu_name, menu_code * menu_price as `연산결과`
	from tbl_menu
    order by `연산결과`;

select category_code, category_name, ref_category_code
	from tbl_category
	order by ref_category_code is null; -- is null은 asc 정렬 시 null을 맨 끝으로 정렬 (숫자나 스트링은 오름차순 정렬)

select category_code, category_name, ref_category_code
	from tbl_category
	order by ref_category_code desc;

select category_code, category_name, ref_category_code
	from tbl_category
	order by ref_category_code is null desc; -- desc 정렬 시 null이 맨 끝 but, is null desc는 null이 맨 앞

select category_code, category_name, ref_category_code
	from tbl_category
	order by ref_category_code is null desc, ref_category_code desc;
    

