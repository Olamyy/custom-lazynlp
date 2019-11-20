from lazynlp import download_page


link = "https://www.nairaland.com/"
max_count = 13


for link_id in range(max_count, 16):
    page = f"{link}{link_id}"
    txt = download_page(page)
    print(f"Reading article:{link_id}..")
    with open(f'nairaland/{link_id}.txt', 'w') as out:
        print(f"Writing article:{link_id} to nairaland/{link_id}.txt'.")
        out.write(page + '\n' + str(txt[1]))

