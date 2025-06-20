import os


def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name: {filename} Created Successfully!")
    except FileExistsError:
        print(f"File Name: {filename} already exists!")
    except Exception as e:
        print("An error occurred:", e)


def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found!")
    else:
        print("Files in Directory:")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as e:
        print("Error:", e)


def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as e:
        print("Error:", e)


def main():
    while True:
        print("\nFile Management App")
        print("1: Create File")
        print("2: View All Files")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit\n")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            filename = input("Enter file name to create: ")
            create_file(filename)
        elif choice == 2:
            view_all_files()
        elif choice == 3:
            filename = input("Enter file name to delete: ")
            delete_file(filename)
        elif choice == 4:
            filename = input("Enter file name to read: ")
            read_file(filename)
        elif choice == 5:
            filename = input("Enter file name to edit: ")
            edit_file(filename)
        elif choice == 6:
            print("Closing the app...")
            break
        else:
            print("Invalid choice! Please select from 1 to 6.")


if __name__ == "__main__":
    main()
