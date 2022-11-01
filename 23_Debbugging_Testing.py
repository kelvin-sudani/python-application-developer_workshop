import pdb

first_name = "John"
last_name = "Doe"
# pdb.set_trace()
breakpoint()
email = first_name+last_name+"@gmail.com"
profile = {"name": firt_name+" "+last_name, "email": email}
print(profile)


# PDB commands:
# l => list
# n => next line
# s => step into function call
# p => print
# c => continue
# q  => quit
# b => list breakpoints
# b 10 => set a breakpoint at line 10 
