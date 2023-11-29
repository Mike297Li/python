def my_function():
    print("Function inside module")

print("Module name:", __name__)

if __name__ == "__main__":
    print("This will only run if the script is executed directly")
