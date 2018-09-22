#1.The first step is to create a list of tuples, which we will use to test our sorting.

employee_records = [ ('joe',1,53),('beck',2,26), \
                     ('ele',6,32),('neo',3,45),  \
                    ('christ',5,33),('trinity',4,29), \
                    ]

# 2.Let us now sort it by employee name
print sorted(employee_records,key=lambda emp : emp[0])
"""
It prints as follows
[('beck', 2, 26), ('christ', 5, 33), ('ele', 6, 32), ('joe', 1, 53), ('neo', 3, 45), ('trinity', 4, 29)]
"""
# 3.Let us now sort it by employee id
print sorted(employee_records,key=lambda emp : emp[1])
"""
It prints as follows
[('joe', 1, 53), ('beck', 2, 26), ('neo', 3, 45), ('trinity', 4, 29), ('christ', 5, 33), ('ele', 6, 32)]
"""
# 4.Finally we sort it with employee age
print sorted(employee_records,key=lambda emp : emp[2])
"""
Its prints as follows
[('beck', 2, 26), ('trinity', 4, 29), ('ele', 6, 32), ('christ', 5, 33), ('neo', 3, 45), ('joe', 1, 53)]
"""
