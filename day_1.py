import pandas as pd

# Import file and create data file 
file_path = '/home/matteo/Desktop/github_repos/advent_of_code_2024/day_1_data.txt'
df = pd.read_csv(file_path, sep = '\s+', header = None)

# Problem 1
def distance(df):
    # Create arrays per each column
    arrays = [df[i].to_numpy() for i in range(df.shape[1])]
    left_column = arrays[0].tolist()
    right_column = arrays[1].tolist()

    # Initialize distance
    dist = 0
    
    # Compute distance
    while left_column:
        # Find minimum value of each column
        min_left = min(left_column)
        min_right = min(right_column)

        # Update distance value
        dist += abs(min_left - min_right)

        # Remove elements from list
        left_column.remove(min_left)
        right_column.remove(min_right)
    
    return dist

# Problem 2
def similarity(df):
    # Create arrays per each column
    arrays = [df[i].to_numpy() for i in range(df.shape[1])]
    left_column = arrays[0].tolist()
    right_column = arrays[1].tolist()

    # Initialize distance
    sim = 0
    
    # Compute distance
    for i in range(len(left_column)):
        # Count times
        multiplicity = right_column.count(left_column[i])

        # Similarity
        sim += left_column[i] * multiplicity
    
    return sim

# Print out distance 
dist = distance(df)
print(f'The distance between the two columns is {dist}')

# Print out similarity
sim = similarity(df)
print(f'The similarity between the two columns is {sim}')
