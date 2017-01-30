# Know-your-neighborhood

Story
A client came and asked about a software for displaying information about cities, towns and villages in Małopolska. Good news is that he is providing data file (Link (Links to an external site.)). Bad news, he's totally newbie when it comes to IT and is interesting only in results. ASAP results, to be more precised. 

 

The exercise
Please:

  I. Define what classes you'll implement in the system.

 II. Draw UML Class diagram.

III. Create a python program that suits client's needs.

 

Required functionality
1. Main menu:

$python main.py
What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities 
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program

Option: 1 
/---------------------------------\
|       MAŁOPOLSKIE               |
|-----+---------------------------|
|   1 | wojewódźtwo               |
|-----+---------------------------|
|  22 | powiaty                   |
|-----+---------------------------|
|  14 | gmina miejska             |
|-----+---------------------------|
| 122 | gmina wiejska             |
|-----+---------------------------|
|  46 | gmina miejsko-wiejska     |
|-----+---------------------------|
|  46 | obszar wiejski            |
|-----+---------------------------|
|  46 | miasto                    |
|-----+---------------------------|
|   3 | miasto na prawach powiatu |
|-----+---------------------------|
|   4 | delegatura                |
\---------------------------------/

Option:  5
Searching for: Nowy

Found 7 location(s):
/------------------------------------------\
| LOCATION     | TYPE                      |
|--------------+---------------------------|
| Nowy Sącz    | gmina miejska             |
| Nowy Sącz    | miasto na prawach powiatu |
| Nowy Targ    | gmina miejska             |
| Nowy Targ    | gmina wiejska             |
| Nowy Wiśnicz | gmina miejsko-wiejska     |
| Nowy Wiśnicz | miasto                    |
| Nowy Wiśnicz | obszar wiejski            |
\------------------------------------------/

(Please notice, that locations are sorted in ascending order, and types are also sorted ascending within the same location)
Rubric

