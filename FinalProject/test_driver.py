from supplier_library import suppliers

roborio = suppliers.andymark_item("am-3000")
neo = suppliers.rev_item("rev-21-1650")

print(roborio.get_name())
print(roborio.get_price())
print(neo.get_name())
print(neo.get_price())