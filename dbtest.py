from table import Table

if __name__ == '__main__':
    parts = Table.read('parts.txt')
    print(parts)
    suppliers = Table.read('suppliers.txt')
    print(suppliers)
    spj = Table.read('spj.txt')
    print(spj)
    projects = Table.read('projects.txt')
    print(projects)
    print(Table.join(parts,spj))
    #print(Table.join(suppliers,spj))
    #print(Table.join(projects,spj))
    print(parts.fields)
    print()
    print(parts.select('pno','p2'))
    print(parts.project('pname','color'))
    print(parts.project('color'))
    print(Table.join(spj, projects))

    suppliers.write('supp2.txt')
    del suppliers
    suppliers = Table.read('supp2.txt')
    print(suppliers)
    projects.store()
    del projects
    projects = Table.restore('projects.db')
    print(projects)

    projects.remove('city','Athens')
    projects.insert('j11','Disk','Baltimore')
    print(projects)
    
    print(Table.join(spj,projects))
    
# Expected output shown below.
''' Output:
parts('pno', 'pname', 'color', 'weight', 'city')
=====
('p2', 'Bolt', 'Green', '17', 'Paris')
('p1', 'Nut', 'Red', '12', 'London')
('p5', 'Cam', 'Blue', '12', 'Paris')
('p6', 'Cog', 'Red', '19', 'London')
('p3', 'Screw', 'Blue', '17', 'Rome')
('p4', 'Screw', 'Red', '14', 'London')

suppliers('sno', 'sname', 'status', 'city')
=========
('s2', 'Jones', '10', 'Paris')
('s5', 'Adams', '30', 'Athens')
('s1', 'Smith', '20', 'London')
('s3', 'Blake', '30', 'Paris')
('s4', 'Clark', '20', 'London')

spj('sno', 'pno', 'jno', 'qty')
===
('s4', 'p6', 'j3', '300')
('s1', 'p1', 'j1', '200')
('s2', 'p3', 'j7', '800')
('s3', 'p4', 'j2', '500')
('s5', 'p2', 'j4', '100')
('s5', 'p6', 'j2', '200')
('s2', 'p3', 'j5', '600')
('s2', 'p3', 'j3', '200')
('s5', 'p6', 'j4', '500')
('s5', 'p5', 'j5', '500')
('s5', 'p3', 'j4', '200')
('s5', 'p5', 'j4', '400')
('s2', 'p3', 'j2', '200')
('s5', 'p2', 'j2', '200')
('s1', 'p1', 'j4', '700')
('s2', 'p3', 'j4', '500')
('s5', 'p1', 'j4', '100')
('s2', 'p3', 'j1', '400')
('s2', 'p5', 'j2', '100')
('s3', 'p3', 'j1', '200')
('s5', 'p4', 'j4', '800')
('s4', 'p6', 'j7', '300')
('s5', 'p5', 'j7', '100')
('s2', 'p3', 'j6', '400')

projects('jno', 'jname', 'city')
========
('j1', 'Sorter', 'Paris')
('j5', 'Collator', 'London')
('j6', 'Terminal', 'Oslo')
('j4', 'Console', 'Athens')
('j7', 'Tape', 'London')
('j3', 'Reader', 'Athens')
('j2', 'Punch', 'Rome')

result('pno', 'pname', 'color', 'weight', 'city', 'sno', 'jno', 'qty')
======
('p3', 'Screw', 'Blue', '17', 'Rome', 's2', 'j6', '400')
('p3', 'Screw', 'Blue', '17', 'Rome', 's3', 'j1', '200')
('p2', 'Bolt', 'Green', '17', 'Paris', 's5', 'j4', '100')
('p5', 'Cam', 'Blue', '12', 'Paris', 's5', 'j7', '100')
('p6', 'Cog', 'Red', '19', 'London', 's5', 'j2', '200')
('p3', 'Screw', 'Blue', '17', 'Rome', 's2', 'j3', '200')
('p6', 'Cog', 'Red', '19', 'London', 's5', 'j4', '500')
('p6', 'Cog', 'Red', '19', 'London', 's4', 'j7', '300')
('p3', 'Screw', 'Blue', '17', 'Rome', 's2', 'j2', '200')
('p4', 'Screw', 'Red', '14', 'London', 's3', 'j2', '500')
('p5', 'Cam', 'Blue', '12', 'Paris', 's5', 'j5', '500')
('p1', 'Nut', 'Red', '12', 'London', 's1', 'j1', '200')
('p3', 'Screw', 'Blue', '17', 'Rome', 's2', 'j5', '600')
('p3', 'Screw', 'Blue', '17', 'Rome', 's5', 'j4', '200')
('p5', 'Cam', 'Blue', '12', 'Paris', 's5', 'j4', '400')
('p5', 'Cam', 'Blue', '12', 'Paris', 's2', 'j2', '100')
('p1', 'Nut', 'Red', '12', 'London', 's1', 'j4', '700')
('p1', 'Nut', 'Red', '12', 'London', 's5', 'j4', '100')
('p3', 'Screw', 'Blue', '17', 'Rome', 's2', 'j4', '500')
('p2', 'Bolt', 'Green', '17', 'Paris', 's5', 'j2', '200')
('p3', 'Screw', 'Blue', '17', 'Rome', 's2', 'j7', '800')
('p6', 'Cog', 'Red', '19', 'London', 's4', 'j3', '300')
('p4', 'Screw', 'Red', '14', 'London', 's5', 'j4', '800')
('p3', 'Screw', 'Blue', '17', 'Rome', 's2', 'j1', '400')

result('sno', 'sname', 'status', 'city', 'pno', 'jno', 'qty')
======
('s4', 'Clark', '20', 'London', 'p6', 'j3', '300')
('s5', 'Adams', '30', 'Athens', 'p1', 'j4', '100')
('s2', 'Jones', '10', 'Paris', 'p3', 'j2', '200')
('s2', 'Jones', '10', 'Paris', 'p5', 'j2', '100')
('s3', 'Blake', '30', 'Paris', 'p4', 'j2', '500')
('s1', 'Smith', '20', 'London', 'p1', 'j4', '700')
('s2', 'Jones', '10', 'Paris', 'p3', 'j3', '200')
('s3', 'Blake', '30', 'Paris', 'p3', 'j1', '200')
('s5', 'Adams', '30', 'Athens', 'p5', 'j5', '500')
('s4', 'Clark', '20', 'London', 'p6', 'j7', '300')
('s2', 'Jones', '10', 'Paris', 'p3', 'j7', '800')
('s5', 'Adams', '30', 'Athens', 'p6', 'j2', '200')
('s5', 'Adams', '30', 'Athens', 'p2', 'j4', '100')
('s2', 'Jones', '10', 'Paris', 'p3', 'j5', '600')
('s5', 'Adams', '30', 'Athens', 'p5', 'j4', '400')
('s2', 'Jones', '10', 'Paris', 'p3', 'j6', '400')
('s1', 'Smith', '20', 'London', 'p1', 'j1', '200')
('s5', 'Adams', '30', 'Athens', 'p2', 'j2', '200')
('s2', 'Jones', '10', 'Paris', 'p3', 'j1', '400')
('s5', 'Adams', '30', 'Athens', 'p4', 'j4', '800')
('s5', 'Adams', '30', 'Athens', 'p5', 'j7', '100')
('s5', 'Adams', '30', 'Athens', 'p6', 'j4', '500')
('s2', 'Jones', '10', 'Paris', 'p3', 'j4', '500')
('s5', 'Adams', '30', 'Athens', 'p3', 'j4', '200')

result('jno', 'jname', 'city', 'sno', 'pno', 'qty')
======
('j1', 'Sorter', 'Paris', 's2', 'p3', '400')
('j7', 'Tape', 'London', 's5', 'p5', '100')
('j4', 'Console', 'Athens', 's5', 'p2', '100')
('j7', 'Tape', 'London', 's2', 'p3', '800')
('j6', 'Terminal', 'Oslo', 's2', 'p3', '400')
('j7', 'Tape', 'London', 's4', 'p6', '300')
('j2', 'Punch', 'Rome', 's2', 'p5', '100')
('j4', 'Console', 'Athens', 's5', 'p4', '800')
('j4', 'Console', 'Athens', 's2', 'p3', '500')
('j4', 'Console', 'Athens', 's5', 'p1', '100')
('j5', 'Collator', 'London', 's5', 'p5', '500')
('j1', 'Sorter', 'Paris', 's3', 'p3', '200')
('j2', 'Punch', 'Rome', 's3', 'p4', '500')
('j4', 'Console', 'Athens', 's5', 'p3', '200')
('j4', 'Console', 'Athens', 's5', 'p5', '400')
('j2', 'Punch', 'Rome', 's5', 'p6', '200')
('j4', 'Console', 'Athens', 's1', 'p1', '700')
('j5', 'Collator', 'London', 's2', 'p3', '600')
('j2', 'Punch', 'Rome', 's5', 'p2', '200')
('j3', 'Reader', 'Athens', 's4', 'p6', '300')
('j2', 'Punch', 'Rome', 's2', 'p3', '200')
('j4', 'Console', 'Athens', 's5', 'p6', '500')
('j3', 'Reader', 'Athens', 's2', 'p3', '200')
('j1', 'Sorter', 'Paris', 's1', 'p1', '200')

('pno', 'pname', 'color', 'weight', 'city')

result('pno', 'pname', 'color', 'weight', 'city')
======
('p2', 'Bolt', 'Green', '17', 'Paris')

result('pname', 'color')
======
('Nut', 'Red')
('Cam', 'Blue')
('Cog', 'Red')
('Screw', 'Blue')
('Screw', 'Red')
('Bolt', 'Green')

result('color',)
======
('Blue',)
('Red',)
('Green',)

suppliers('sno', 'sname', 'status', 'city')
=========
('s2', 'Jones', '10', 'Paris')
('s5', 'Adams', '30', 'Athens')
('s1', 'Smith', '20', 'London')
('s3', 'Blake', '30', 'Paris')
('s4', 'Clark', '20', 'London')

projects('jno', 'jname', 'city')
========
('j1', 'Sorter', 'Paris')
('j5', 'Collator', 'London')
('j6', 'Terminal', 'Oslo')
('j4', 'Console', 'Athens')
('j7', 'Tape', 'London')
('j3', 'Reader', 'Athens')
('j2', 'Punch', 'Rome')

projects('jno', 'jname', 'city')
========
('j1', 'Sorter', 'Paris')
('j5', 'Collator', 'London')
('j6', 'Terminal', 'Oslo')
('j7', 'Tape', 'London')
('j11', 'Disk', 'Baltimore')
('j2', 'Punch', 'Rome')

result('sno', 'pno', 'jno', 'qty', 'jname', 'city')
======
('s2', 'p3', 'j1', '400', 'Sorter', 'Paris')
('s2', 'p3', 'j7', '800', 'Tape', 'London')
('s2', 'p3', 'j6', '400', 'Terminal', 'Oslo')
('s2', 'p3', 'j2', '200', 'Punch', 'Rome')
('s5', 'p5', 'j5', '500', 'Collator', 'London')
('s1', 'p1', 'j1', '200', 'Sorter', 'Paris')
('s4', 'p6', 'j7', '300', 'Tape', 'London')
('s5', 'p2', 'j2', '200', 'Punch', 'Rome')
('s5', 'p5', 'j7', '100', 'Tape', 'London')
('s3', 'p4', 'j2', '500', 'Punch', 'Rome')
('s2', 'p3', 'j5', '600', 'Collator', 'London')
('s3', 'p3', 'j1', '200', 'Sorter', 'Paris')
('s5', 'p6', 'j2', '200', 'Punch', 'Rome')
('s2', 'p5', 'j2', '100', 'Punch', 'Rome')
'''
