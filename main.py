"""This is the main file, the one that should be executed"""


# libraries
import os
import re
import time as tm
import sys


# local file
import config
import scraping as scrap
import data_base as db


def main():

    # initial display
    initial_display()

    # load config
    destination = config.destination

    # initialise the connection with the data base (and create it if needed)
    connection = db.main()

    # initialize scraping
    browser = scrap.initialise_scraping(destination)
    success = scrap.connect_to_bigfoot(browser)
    if not success:
        return False

    # load watch liste
    with open(".\watch_list.txt", "r", encoding="UTF-8") as file:
        watch_list = file.read().splitlines()


    # set up internal use
    report = {
        "failed": [],
        "downloaded": [],
        "already_downloaded": [],
        "not_on_bigfoot": [],
    }

    # main loop
    try:
        for title in watch_list:
            # try to download the movie
            status = download(browser, connection, title, destination)
            report[status] += [title]

        browser.close()
        report_to_user(report)

    except KeyboardInterrupt:
        report_to_user(report)
        browser.close()
        sys.exit()

    except Exception as e:
        print("error", e)
        browser.close()


def initial_display():
    os.system("cls")
    print(
        "\n#################################################################################\n",
        "                       BIGFOOT DL (V 1.0)"
        "\n#################################################################################\n\n"
        "Initialisation [Working]",
    )


def report_to_user(report):
    # Inform user
    downloaded = " / ".join(report["downloaded"])
    failed = " / ".join(report["failed"])
    not_on_bigfoot = " / ".join(report["not_on_bigfoot"])

    print(
        "\n#################################################################################\n",
        "Report: \n",
        f"   - downloaded: {downloaded}\n",
        f"   - failed: {failed}\n",
        f"   - not on bigfoot: {not_on_bigfoot}",
        "\n#################################################################################\n",
    )


def download(browser, connection, title, destination):
    """
    Try to download the movie
    and add it in the database if this is not already done
    """

    # check if movie isn't already downloaded
    if not db.is_movie_downloaded(connection, title):
        res = scrap.download_movie(browser, title)

        # scraping error
        if res == None:
            status = "failed"

        # no scraping error
        else:
            succes, result = res

            # not on bigfoot case or sythaxe error (from user)
            if not succes:
                others = " / ".join(result[:3])
                print(f"{title} is not on bigfoot !")
                print(f"Maybe this could interest you: {others}")
                status = "not_on_bigfoot"

            # downloading case
            else:
                status = "downloaded"
                wait_download(result, destination)
                db.add_download(connection, (title, result["Year"]))

    # already downloaded case
    else:
        print(f"{title} has already been donwloaded, just skipping")
        status = "already_downloaded"

    return status


def wait_download(result, destination):
    """
    Wait during the donwloading a the movie.
    Then rename it

    The function is quite comple because there is diffrent type of file and diffrent behaviour
    """

    list_dir = os.listdir(destination)
    list_movie_og = re.findall(".*.crdownload", "\n".join(list_dir))
    list_movie = list_movie_og.copy()

    n, = len(list_movie)
    title = result["Title"]
    year = result["Year"]

    # While download is not done yet
    while len(list_movie) == n :
        list_dir = os.listdir(destination)
        list_movie = re.findall(".*.crdownload", "\n".join(list_dir))
        for k in range(4):
            print(f"Downloading {title} " + k * "." + "     " + "\r", end="")
            tm.sleep(0.5)
            
    movie = set(list_movie_og).difference(set(list_movie))
    movie = list(movie)[0][:-11]
    os.rename(
        destination + "\\" + movie,
        destination + "\\" + title + movie[-4:],
    )

    print(f"{title} succesfully downloaded ! ")
    
 
def remove_space(title):
    if title[-1] == " ":
        return remove_space(title[:-1])
    else:
        return title


if __name__ == "__main__":
    main()
