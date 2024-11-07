from user import User
person=User('otabek','Abdurasulov',17,'student')

def test_1():
    assert person.name=='otabek'
    assert person.surname=='Abdurasulov'
    assert person.age==17
    assert person.accupation=='student'
test_1()