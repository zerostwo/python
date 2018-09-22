# Let us now enclose the employee records as class objects,
class employee(object):
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    def pretty_print(self):
       print self.name,self.id,self.age

# Now let us populate a list with these class objects.
employee_records = []
emp1 = employee('joe',1,53)
emp2 = employee('beck',2,26)
emp3 = employee('ele',6,32)

employee_records.append(emp1)
employee_records.append(emp2)
employee_records.append(emp3)

# Print the records
for emp in employee_records:
    emp.pretty_print()


from operator import attrgetter
employee_records_sorted = sorted(employee_records,key=attrgetter('age'))
# Now let us print the sorted list,
for emp in employee_records_sorted:
    emp.pretty_print()
