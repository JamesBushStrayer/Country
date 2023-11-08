# Name: James Alan Bush
# Course Number: CIS261005VA016-1238-001
# Assignment Title: Country


def display_menu():
  print("\nCountry Menu")
  print("1. View a Country")
  print("2. Add a Country")
  print("3. Delete a Country")
  print("4. Exit")


def view_country(country_dict):
  print("\nAvailable country keys:")
  for key in country_dict.keys():
    print(key)
  choice = input("\nEnter a key: ")
  if choice in country_dict:
    print(f"The country for key {choice} is {country_dict[choice]}")
  else:
    print(f"\n{choice} is an invalid key")


def add_country(country_dict):
  new_key = input("\nEnter a new key: ")
  if new_key in country_dict:
    print(f"\n{new_key} already exists!")
  else:
    new_name = input("Enter a new country name: ")
    country_dict[new_key] = new_name
    print(f"\n{new_name} added")


def delete_country(country_dict):
  del_key = input("\nEnter a key to delete: ")
  if del_key in country_dict:
    del country_dict[del_key]
    print(f"\n{del_key} deleted")
  else:
    print(f"\n{del_key} is an invalid key")


def main():
  country_dict = {
      "us": "United States",
      "uk": "United Kingdom",
      "de": "Germany"
  }

  while True:
    display_menu()
    choice = input("\nChoose a command: ")
    if choice == "1":
      view_country(country_dict)
    elif choice == "2":
      add_country(country_dict)
    elif choice == "3":
      delete_country(country_dict)
    elif choice == "4":
      print("\nExiting program.")
      break
    else:
      print(f"\n{choice} is an invalid command!")


if __name__ == "__main__":
  main()
