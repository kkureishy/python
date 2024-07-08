#main function
def main():
    #list of top artists
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    #counter set at 1
    count = 1
    #loop through top_artists list and print each artist numbered
    for i in top_artists:
        print(str(count) + ". " + i)
        count+=1 
    try: #try to input the index of the artist you want to replace
        index = int(input("Enter the index of the artist you want to replace: "))
        #subtract index minus 1 to get python index
        x= index-1
        #get the artist at request index
        name = top_artists[x]
    except (IndexError, ValueError): #if index is outside of list or not a integer let user know
        print("An input error occurred.")
    else: #if not remove artist and replace with new artist 
        top_artists.remove(name)
        input2 = input("Enter the name of the new artist: ")
        top_artists.insert(x, input2)   
        #reprint list
        count = 1
        for i in top_artists:
            print(str(count) + ". " + i)
            count+=1
#call main function
main()