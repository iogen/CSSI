form = """
To: [name]
Address: [address]

Hello, [name].

I hope you are having a good day at CSSI.

Yours sincerely,
Thomas

[date]
"""

name = raw_input("Enter name: ")
address = raw_input("Enter address: ")
date = raw_input("Enter address: ")



form = form.replace("[name]",name)
form = form.replace("[address]",address)
form = form.replace("[date]",date)

print [form]
