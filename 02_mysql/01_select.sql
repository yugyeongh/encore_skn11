use menudb;
-- select from
select menu_name from tbl_menu;

select menu_code, menu_name, menu_price, category_code, orderable_status from tbl_menu;

select * from tbl_menu;

select 12+17; -- oracle에서는 select은 꼭 from과 써야함
select 12-17;
select 12*17;
select 12/17;
select 12%17;