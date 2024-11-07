from user import User
person=User('otabek','Abdurasulov',17,'udent')

def test_1():
    assert person.name=='otabek'
    assert person.surname=='Abdurasulov'
    
test_1()