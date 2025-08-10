from functions.get_files_info import get_files_info



def tests():
    test_list = [
        ".", "pkg", "/bin", "../"
    ]
    for item in test_list:
        if item == ".":
            print(f"Result for current directory:\n{get_files_info("calculator", item)}")
        else:
            print(f"Result for '{item}' directory:\n{get_files_info("calculator", item)}")


if __name__ == "__main__":
    tests()