import main2


def serialize_movies():
    movies = main.read_json_file()
    output = ""
    for key, value in movies.items():
        output += "    <li>\n"
        output += "        <div class='movie'>\n"
        if "N/A" != value['poster']:
            output += f"            <img class='movie-poster'\n" \
                      f"            src='{value['poster']}'\n" \
                      f"            title= ''/>\n"
        output += f"            <div class='movie-title'>{key}</div>\n"
        output += f"            <div class='movie-rating'>{value['rating']}</div>\n"
        output += f"            <div class='movie-year'>{value['year']}</div>\n"
        output += '        </div>\n'
        output += '    </li>\n'
    return output


def generate_html():
    output = serialize_movies()
    title_html = "Movie Database"
    with open("index_template.html", "r") as handle1:
        data2 = handle1.read()

    try:
        with open("index.html", "w") as handle2:
            handle2.write(data2.replace("__TEMPLATE_TITLE__", title_html)
                          .replace("__TEMPLATE_MOVIE_GRID__", output))
            print("Website generated successfully ")
    except Exception:
        print("Error Generating Website")

