import pytest

def test_add_new_element_empty_list(monkeypatch):
    from utils import addNewElement
    
    inputs = iter(['John Doe', '123-456-7890', 'john@example.com', 'Group A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    students = []
    
    updated_students = addNewElement(students)
    
    assert len(updated_students) == 1
    assert updated_students[0]['name'] == 'John Doe'
    assert updated_students[0]['phone'] == '123-456-7890'
    assert updated_students[0]['email'] == 'john@example.com'
    assert updated_students[0]['group'] == 'Group A'

def test_add_new_element_with_predefined_dict():
    from utils import addNewElement
    
    students = [
        {'name': 'Alice', 'phone': '111-111-1111', 'email': 'alice@example.com', 'group': 'Group B'}
    ]
    
    new_student = {'name': 'Bob', 'phone': '222-222-2222', 'email': 'bob@example.com', 'group': 'Group A'}
    
    updated_students = addNewElement(students, new_student)
    
    assert len(updated_students) == 2
    assert updated_students[0]['name'] == 'Alice'
    assert updated_students[1]['name'] == 'Bob'

def test_delete_element_by_position():
    from utils import deleteElement
    
    students = [
        {'name': 'Alice', 'phone': '111-111-1111', 'email': 'alice@example.com', 'group': 'Group A'},
        {'name': 'Bob', 'phone': '222-222-2222', 'email': 'bob@example.com', 'group': 'Group B'}
    ]
    
    updated_students = deleteElement(students, 1)
    
    assert len(updated_students) == 1
    assert updated_students[0]['name'] == 'Alice'

def test_delete_element_by_name(monkeypatch):
    from utils import deleteElement
    
    students = [
        {'name': 'Alice', 'phone': '111-111-1111', 'email': 'alice@example.com', 'group': 'Group A'},
        {'name': 'Bob', 'phone': '222-222-2222', 'email': 'bob@example.com', 'group': 'Group B'}
    ]
    
    monkeypatch.setattr('builtins.input', lambda _: 'Alice')
    
    updated_students = deleteElement(students)
    
    assert len(updated_students) == 1
    assert updated_students[0]['name'] == 'Bob'

def test_delete_element_not_found(monkeypatch, capsys):
    from utils import deleteElement
    
    students = [
        {'name': 'Alice', 'phone': '111-111-1111', 'email': 'alice@example.com', 'group': 'Group A'}
    ]
    
    monkeypatch.setattr('builtins.input', lambda _: 'Bob')
    
    updated_students = deleteElement(students)
    
    captured = capsys.readouterr()
    
    assert captured.out.strip() == "Element was not found"
    assert len(students) == 1 

def test_update_element(monkeypatch):
    from utils import updateElement
    
    students = [
        {'name': 'Alice', 'phone': '111-111-1111', 'email': 'alice@example.com', 'group': 'Group A'}
    ]
    
    inputs = iter(['Alice', 'New Alice', '999-999-9999', 'new.alice@example.com', 'Group B'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    updated_students = updateElement(students)
    
    assert len(updated_students) == 1
    assert updated_students[0]['name'] == 'New Alice'
    assert updated_students[0]['phone'] == '999-999-9999'
    assert updated_students[0]['email'] == 'new.alice@example.com'
    assert updated_students[0]['group'] == 'Group B'

def test_print_all_list(capsys):
    from utils import printAllList
    
    students = [
        {'name': 'Alice', 'phone': '111-111-1111', 'email': 'alice@example.com', 'group': 'Group A'}
    ]
    
    printAllList(students)
    
    captured = capsys.readouterr()
    

    expected_output = "Student name is Alice, phone is 111-111-1111, email is alice@example.com and group is Group A;"
    assert captured.out.strip() == expected_output

def test_delete_from_empty_list(capsys):
    from utils import deleteElement
    
    students = []
    
    def mock_input(_):
        return 'Test'
    
    deleteElement(students)
    
    captured = capsys.readouterr()
    
    assert captured.out.strip() == "there are no elements in the database"