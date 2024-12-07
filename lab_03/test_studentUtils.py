import pytest
from studentUtils import StudentUtils, StudentNotFoundError, StudentExistsError


class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __repr__(self):
        return f"Student(name={self.name}, phone={self.phone}, email={self.email}, group={self.group})"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.name == other.name and self.phone == other.phone and self.email == other.email and self.group == other.group


@pytest.fixture
def setup_students():
    student1 = Student(name="Alice", phone="123456789", email="alice@example.com", group="A1")
    student2 = Student(name="Bob", phone="987654321", email="bob@example.com", group="B2")
    student3 = Student(name="Charlie", phone="555555555", email="charlie@example.com", group="C3")
    utils = StudentUtils(students=[student1, student2])
    return utils, student1, student2, student3


def test_add_new_student(setup_students):
    utils, _, _, student3 = setup_students
    utils.addNewStudent(student3)
    assert student3 in utils.students


def test_add_existing_student_raises_error(setup_students):
    utils, student1, _, _ = setup_students
    with pytest.raises(StudentExistsError):
        utils.addNewStudent(student1)


def test_delete_existing_student(setup_students):
    utils, student1, _, _ = setup_students
    utils.delStudent("Alice")
    assert student1 not in utils.students


def test_delete_nonexistent_student_raises_error(setup_students):
    utils, _, _, _ = setup_students
    with pytest.raises(StudentNotFoundError):
        utils.delStudent("Nonexistent")


def test_edit_existing_student(monkeypatch, setup_students):
    utils, student1, _, _ = setup_students

    def mock_input(prompt):
        if "phone" in prompt:
            return "111111111"
        elif "email" in prompt:
            return "newalice@example.com"
        return ""

    monkeypatch.setattr("builtins.input", mock_input)
    utils.editStudent("Alice")

    assert utils.students[0].phone == "111111111"
    assert utils.students[0].email == "newalice@example.com"


def test_edit_nonexistent_student_raises_error(setup_students):
    utils, _, _, _ = setup_students
    with pytest.raises(StudentNotFoundError):
        utils.editStudent("Nonexistent")


def test_sort_students(setup_students):
    utils, _, _, student3 = setup_students
    utils.addNewStudent(student3)
    sorted_names = [student.name for student in utils.students]
    assert sorted_names == ["Alice", "Bob", "Charlie"]


def test_is_exists(setup_students):
    utils, _, _, _ = setup_students
    assert utils._StudentUtils__isExists("Alice") == 0
    assert utils._StudentUtils__isExists("Nonexistent") == -1
