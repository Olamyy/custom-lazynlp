link = "https://www.nairaland.com/"

max_count = 13


with open('small_urls.txt', 'w+') as fi:
    for link_id in range(max_count, 16):
        page = f"{link}{link_id}"
        print(f"Writing article:{link_id} to file.")
        fi.write("%s\n" % page)
