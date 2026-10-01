# print("MINI PRO 1")
# print("\n TASK 1: Custom Playlist Iterator")

# class PlaylistIterator:
#     def __init__(self, songs):
#         self.songs = songs
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         # Play current song, then move forward
#         song = self.songs[self.index]
#         self.index = (self.index + 1) % len(self.songs)  # loop back at end
#         return song

#     def previous(self):
#         # Move back one song, loop to end if at start
#         self.index = (self.index - 1) % len(self.songs)
#         return self.songs[self.index]


# # Example usage
# playlist = PlaylistIterator(["Song A", "Song B", "Song C"])

# print("Playing songs in order:")
# for i in range(5):   # play more than length to show looping
#     print(next(playlist))

# print("\nGo back to previous song:")
# print(playlist.previous())
# print(playlist.previous())

# print("MINI PRO 2")
# print("\n TASK 2: Batch Data Processor")

# class BatchDataIterator:
#     def __init__(self, data, batch_size=5):
#         self.data = data
#         self.batch_size = batch_size
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.data):
#             # Slice the next batch
#             batch = self.data[self.index:self.index + self.batch_size]
#             self.index += self.batch_size
#             return batch
#         else:
#             raise StopIteration   # gracefully stop when no more data


# # Example usage
# student_records = [
#     {"name": "Alice", "grade": "A"},
#     {"name": "Bob", "grade": "B"},
#     {"name": "Charlie", "grade": "A"},
#     {"name": "David", "grade": "C"},
#     {"name": "Eva", "grade": "B"},
#     {"name": "Frank", "grade": "A"},
#     {"name": "Grace", "grade": "C"},
# ]

# # Process in batches of 3
# batch_iterator = BatchDataIterator(student_records, batch_size=3)

# for batch in batch_iterator:
#     print("Processing batch:", batch)
print("MINI PRO 3")
print("\n TASK 3: CSV File Data Streamer")

import csv

def csv_reader(filename, condition=None):
    """
    Generator that reads a CSV file line by line.
    :param filename: Path to CSV file
    :param condition: A function that takes a row dict and returns True/False
    """
    with open(filename, "r") as f:
        reader = csv.DictReader(f)   # parses rows into dictionaries
        for row in reader:
            if condition is None or condition(row):
                yield row   # yield one row at a time


# Example usage: filter employees with Salary > 50000
def salary_filter(row):
    return int(row["Salary"]) > 50000

for record in csv_reader("employees.csv", condition=salary_filter):
    print(record)
# print("\n TASK 4: Paginated API Data Fetcher")

# import requests

# def api_data_fetcher(base_url, params=None, page_param="page", start_page=1):
#     """
#     Generator that fetches paginated API data page by page.
#     :param base_url: API endpoint URL
#     :param params: Dictionary of query parameters
#     :param page_param: Name of the page parameter (default 'page')
#     :param start_page: Starting page number
#     """
#     page = start_page
#     while True:
#         # Copy params and add current page
#         query_params = params.copy() if params else {}
#         query_params[page_param] = page

#         response = requests.get(base_url, params=query_params)
#         if response.status_code != 200:
#             print(f"Error: {response.status_code}")
#             break

#         data = response.json()
#         if not data or len(data) == 0:
#             break   # stop when no more data

#         yield data   # yield one page of results
#         page += 1


# # Example usage with demo API
# for page_data in api_data_fetcher(
#     "https://jsonplaceholder.typicode.com/posts",
#     params={}, page_param="_page"
# ):
#     print("Page:", page_data[:2])   # print first 2 items from each page
# print("\n TASK 5: Lazy Loading Image Viewer")

# import os
# from PIL import Image

# def lazy_load_images(folder_path):
#     """
#     Generator that lazily loads images from a folder.
#     :param folder_path: Path to the folder containing images
#     """
#     for filename in os.listdir(folder_path):
#         if filename.lower().endswith((".jpg", ".jpeg", ".png")):
#             file_path = os.path.join(folder_path, filename)
#             yield file_path   # yield one image path at a time


# # Example usage
# folder = r"C:\Users\ADMIN\Desktop\Images"   # change to your folder path

# for img_path in lazy_load_images(folder):
#     print(f"Loading: {img_path}")
#     img = Image.open(img_path)
#     img.show()   # display image using default viewer

#     input("Press Enter to view next image...")

# print("\n TASK 6: Log File Parser")

# def filter_log_entries(filename, keywords=("ERROR", "WARNING")):
#     """
#     Generator that reads a log file line by line
#     and yields only lines containing specified keywords.
#     :param filename: Path to log file
#     :param keywords: Tuple of keywords to filter (default: ERROR, WARNING)
#     """
#     with open(filename, "r") as f:
#         for line in f:
#             if any(keyword in line for keyword in keywords):
#                 yield line.strip()


# # Example usage
# for entry in filter_log_entries("system.log"):
#     print("Filtered Entry:", entry)
