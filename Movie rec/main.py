#Movie recomander Aaron Wang
import csv

#List of stored movie data
movies = []

#Read movie list file and store data
def file_open():
    try:
        with open('Movie rec\Movies list.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                movies.append({
                    "title": row["Title"],
                    "director": row["Director"],
                    "genre": row["Genre"],
                    "rating": row["Rating"],
                    "length": row["Length (min)"],
                    "actors": row["Notable Actors"]
                })
    except FileNotFoundError:
        print("Error: The file 'Movies list.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Print the complete movie list
def print_all_movies():
    index = 1
    if not movies:
        print("No movies available.")
        return
    for movie in movies:
        print(f"{index}.\tTitle: {movie['title']}, Director: {movie['director']}, Genre: {movie['genre']}, "
              f"Rating: {movie['rating']}, Length: {movie['length']} min, Actors: {movie['actors']}")
        index = index + 1

#Filter movies based on user input criteria
def filter_movies(criteria):
    filtered_movies = movies
    for key, value in criteria.items():
        filtered_movies = [movie for movie in filtered_movies if value.lower() in movie[key].lower()]
    return filtered_movies

#Clean up user input
def sanitize_input(user_input):
    return user_input.strip().lower()

#Main function, controls program execution
def main():
    file_open()
    
    while True:
        print("\n1. Search Movies\n2. Show All Movies\n3. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            print("You can filter by:")
            print("1. Title\t2. Director\t3. Genre\t4. Rating\t5. Length\t6. Actors")
            criteria = {}
            for _ in range(2):  #Support 2 search criteria
                filter_type = input("Enter the number for filter type (1-6): ").strip()
                filter_map = {
                    "1": "title",
                    "2": "director",
                    "3": "genre",
                    "4": "rating",
                    "5": "length",
                    "6": "actors"
                }
                if filter_type not in filter_map:
                    print("Invalid filter type. Please try again.")
                    continue
                filter_value = sanitize_input(input(f"Enter the {filter_map[filter_type]} to filter by: "))
                criteria[filter_map[filter_type]] = filter_value
            
            filtered_movies = filter_movies(criteria)
            if filtered_movies:
                print("\nFiltered Movies:")
                index = 1
                for movie in filtered_movies:
                    print(f"{index}.\tTitle: {movie['title']}, Director: {movie['director']}, Genre: {movie['genre']}, "
                          f"Rating: {movie['rating']}, Length: {movie['length']} min, Actors: {movie['actors']}")
                    index = index + 1
            else:
                print("No movies found matching the criteria.")
        elif choice == "2":
            print("\nAll Movies:")
            print_all_movies()
        
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Wrong option. Please try again.")

if __name__ == "__main__":
    main()

