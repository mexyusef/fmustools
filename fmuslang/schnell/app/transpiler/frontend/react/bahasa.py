
react_language = """
program: statement+
statement: 
	| statement_config? statement_choice

// pengennya gimana: bisa generate berbagai versi next/react/mui/bs/dst.
// bisa generate fmus
// bisa generate + execute fmus
statement_config: statement_config_list "/"
statement_config_list: statement_config_item ("," statement_config_item)*
statement_config_item: "*" -> run_fmus
	| "i" -> info // info atau help, mengentai kode yg dioprek
	| "c" -> config_c

// index=list -> product item(s) -> product detail
statement_choice: "a1" -> create_product_model
	| "a2" -> create_product_api // utk dikonversi ke list of product items
	| "a3" -> create_product_item_component // product item, list itu di pages/index
	| "a4" -> create_product_style // display: grid, grid-template-columns: list + detail
	| "a5" -> create_product_detail_page // pages/product/[id]
	| "a6" -> create_add_to_cart_action // product-item tambah button yg panggil action ini
	// button add to cart/buy juga muncul pd product detail page
	// disable button jk in-stock=0
	| "a7" -> add_cart_to_navbar
	| "a8" -> create_cart_page // list cart items + shipping form
	| "a9" -> create_cart_item_component
	| "a10" -> redux_add_to_cart
	| "a11" -> redux_cart_increase_decreate
	| "1" -> setup
	| "2" -> register
	| "3" -> login
	| "4" -> product_list
	| "5" -> product_detail
	| "6" -> cart_create
	| "7" -> cart_update
	| "8" -> cart_delete
	| "9" -> middleware_create_order
	| "10" -> profile_reset_password
	| "11" -> update_avatar_name
	| "12" -> orders
	| "13" -> payment
	| "14" -> admin_order_manager
	| "15" -> admin_user_manager
	| "16" -> admin_category_manager
	| "17" -> admin_create_product
	| "18" -> admin_update_product
	| "19" -> admin_delete_product
	| "20" -> load_more
	| "21" -> filter_sort_search
"""


huruf = """
HURUF_DIGIT: ("_"|LETTER|DIGIT) 	("_"|LETTER|DIGIT|".")*
"""

from langs import base_grammar

bahasa = f"""
{react_language}

{huruf}

{base_grammar}
"""

