import os
import pytest
import csv

def test_read_existing_csv(tmp_path):
    test_file = tmp_path / "test.csv"
    test_data = [
        {"name": "John", "age": "30"},
        {"name": "Jane", "age": "25"}
    ]
    
    with open(test_file, "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(test_data)
    
    from file_handler import readFile
    
    result = readFile(str(test_file))
    
    assert len(result) == 2
    assert result[0]["name"] == "John"
    assert result[0]["age"] == "30"

def test_create_csv_file(tmp_path):
    test_file = tmp_path / "new_file.csv"
    
    from file_handler import createCSVFile
    
    createCSVFile(str(test_file))
    
    assert os.path.exists(test_file)
    
    with open(test_file, 'r', encoding='utf-8') as file:
        content = file.read()
        assert content == ""

def test_save_csv_file(tmp_path):
    test_file = tmp_path / "save_file.csv"
    
    from file_handler import saveCSV
    
    test_data = [
        {"name": "John", "age": "30", "city": "New York"},
        {"name": "Jane", "age": "25", "city": "San Francisco"}
    ]
    
    saveCSV(str(test_file), test_data)
    
    assert os.path.exists(test_file)
    
    with open(test_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        saved_data = list(reader)
        
        assert len(saved_data) == 2
        
        assert saved_data[0]['name'] == "John"
        assert saved_data[0]['age'] == "30"
        assert saved_data[0]['city'] == "New York"

def test_file_not_found_create_file(monkeypatch, tmp_path):
    non_existent_file = tmp_path / "non_existent.csv"
    
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    
    from file_handler import readFile
    
    result = readFile(str(non_existent_file))
    
    assert result == []
    assert os.path.exists(non_existent_file)

def test_file_not_found_exit(monkeypatch):
    from file_handler import readFile
    
    non_existent_file = "/path/to/non/existent/file.csv"
    
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    
    with pytest.raises(SystemExit) as excinfo:
        readFile(non_existent_file)
    
    assert excinfo.value.code == 0

def test_save_csv_empty_data(tmp_path):
    test_file = tmp_path / "empty_save_file.csv"
    
    from file_handler import saveCSV
    
    with pytest.raises(IndexError):
        saveCSV(str(test_file), [])