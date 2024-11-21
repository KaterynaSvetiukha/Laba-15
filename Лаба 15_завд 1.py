import pandas as pd

students = pd.DataFrame({
    "Kateruna Svetiukha": [12, 9, 7, 7, 8, 10, 8, 9, 10, 11],
    "Dmytro Kropyvnytskyi": [7, 12, 11, 8, 4, 9, 10, 6, 7, 8],
    "Daria Mykytenko": [12, 8, 9, 5, 7, 6, 8, 10, 10, 11],
    "Maksym Belik": [9, 11, 12, 10, 7, 8, 6, 9, 10, 12],
    "Vladyslav Ponomariov": [8, 9, 10, 8, 7, 9, 10, 11, 11, 12],
    "Yaroslav Getman": [10, 11, 11, 12, 7, 8, 8, 8, 10, 7],
    "Oleksandr Dvornik": [11, 12, 10, 9, 8, 11, 11, 10, 12, 9],
    "Anna Elnikova": [10, 9, 8, 7, 6, 10, 12, 12, 10, 9],
    "Kyrylo Kyrychenko": [8, 7, 6, 9, 9, 8, 10, 11, 12, 10],
    "Oleksandr Kyslyi": [6, 12, 8, 9, 5, 7, 10, 9, 8, 7]
})

print(students)
print("Yaroslav Getman's grades:", students["Yaroslav Getman"])
print("Average value of Yaroslav Getman's grades:", students["Yaroslav Getman"].mean())
print("Maximum value of Yaroslav Getman's grades:", students["Yaroslav Getman"].max())
print("Minimum value of Yaroslav Getman's grades:", students["Yaroslav Getman"].min())
print("Summa value of Yaroslav Getman's grades:", students["Yaroslav Getman"].sum())
