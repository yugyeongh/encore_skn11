# distinct - 중복되는 값을 하나씩만 뽑기 위해 사용
# 위치는 select과 컬럼명 사이

select distinct category_code
	from tbl_menu
    order by category_code;

select distinct ref_category_code -- 중복을 제외한 값이 나옴 (null도 포함)
	from tbl_category;

select distinct category_code, orderable_status
	from tbl_menu
    order by category_code, orderable_status;