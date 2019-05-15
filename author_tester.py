from author_generator import *

authors_data = [["Ahmet Emin","Mumtaz"], ["Elif","Taylan"], ["Dincer", "Faylan"], ["Dincero", "Faylana"], ["Duygu", "Gaylan"], ["Duru", "Faylan"], ["Elif", "Faylana"]]

a = AuthorGenerator()

formatted_authors=[]
for author_data in authors_data:
    author = a.get_author_with_lastname_commablank_abbreviated_firstname_dot(author_data[0], author_data[1])
    formatted_authors.append(author)

formatted = a.get_author_names_in_apa_format(formatted_authors)
print(formatted)
