mixed_type = {'raghul',54,True,23}
more_add = {'kumar',43}

#add() method -> add element to the set
mixed_type.add('Trainee')
print('Add-Method : ',mixed_type)


#update() method
mixed_type.update(more_add)
print('Update Method : ',mixed_type)

#discard() method -> remove specified element
mixed_type.discard('Trainee')
print('Discard Method : ',mixed_type)


mixed_type.remove('kumar')
print('Remove Method : ',mixed_type)
