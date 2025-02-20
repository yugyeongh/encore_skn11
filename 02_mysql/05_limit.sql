# limit

select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_price desc;

-- offset: 2, row count: 5
select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_price desc
    limit 2,5; # offset(시작하는 행의 번호), 조회해서 가져올 행의 수
    
select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_price desc
    limit 5; # 하나만 작성하면 0부터 시작해서 작성된 숫자만큼 가져옴

select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_price desc
    limit 7;

