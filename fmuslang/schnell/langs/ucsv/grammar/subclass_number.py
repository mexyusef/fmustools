number_subclass_type = """number_subclass_type: "ph"	-> phone_number
| "ccc"					            -> country_calling_code
| "cc"					            -> credit_card_number
| "ccf"					            -> credit_card_full
| "m"					              -> msisdn
| "ssn"					            -> ssn
| "rn" numdigits?           -> random_number
| "ri" min_max? 		        -> random_int				
// python data.py gen data 1 meja hitung:i:ri(-50,60)
| "rd"					            -> random_digit	
| "f"	right_left?           -> pyfloat
| "d"					              -> pydecimal
| "i"					              -> pyint
| "i128"					          -> i128
| "i64"					            -> i64
| "i32"					            -> i32
| "i16"					            -> i16
| "i8"					            -> i8
| "u128"					          -> u128
| "u64"					            -> u64
| "u32"					            -> u32
| "u16"					            -> u16
| "u8"					            -> u8
| "b"                       -> pybool
| "coo"					            -> coordinate
| "lat"					            -> latitude
| "long"				            -> longitude
| "ll"					            -> latlng
| "lll"					            -> local_latlng
| "lol"					            -> location_on_land
"""
