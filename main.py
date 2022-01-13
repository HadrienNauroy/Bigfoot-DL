"""This is the main file, the one that should be executed"""


# libraries
import os
import re
import time as tm
import shutil


# local file
import config
import scraping as scrap
import data_base as db


def main():

    # load config :
    paths = config.downloads, config.destination

    # initialise the connection with the data base (and create it if needed)
    connection = db.main()

    # initialize scraping
    browser = scrap.initialise_scraping()
    success = scrap.connect_to_bigfoot(browser)
    if not success:
        return False

    # load watch liste
    with open(".\watch_list.txt", "r") as file:
        watch_list = file.readlines()

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
            status = download(browser, connection, title, paths)
            report[status] += [title]

        browser.close()
        report_to_user(report)

    except Exception as e:
        print("error", e)
        report_to_user(report)
        browser.close()


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


def download(browser, connection, title, paths):
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
                others = " / ".join(result)
                print(f"{title} is not on bigfoot !")
                print(f"Maybe this could interest you: {others}\n")
                status = "not_on_bigfoot"

            # downloading case
            else:
                status = "downloaded"
                db.add_download(connection, (title, result["Year"]))
                wait_and_moove(result, paths)

    # already downloaded case
    else:
        print(f"{title} has already been donwloaded, just skipping")
        status = "already_downloaded"

    return status


def wait_and_moove(result, paths):
    """
    Wait during the donwloading a the movie.
    Then Movie it from downloads to the destination file
    """

    source, destination = paths
    list_dir = os.listdir(source)
    list_movie_og = re.findall(".*.mp4", "\n".join(list_dir))
    list_movie = list_movie_og.copy()
    n = len(list_movie)
    title = result["Title"]
    year = result["Year"]
    while len(list_movie) == n:
        list_dir = os.listdir(source)
        list_movie = re.findall(".*.mp4", "\n".join(list_dir))
        for k in range(4):
            print(f"Downloading {title} " + k * "." + "     " + "\r", end="")
            tm.sleep(0.5)

    movie = set(list_movie).difference(set(list_movie_og))
    movie = list(movie)[0]
    shutil.move(source + "\\" + movie, destination + "\\" + title + "_" + year + ".mp4")
    print(f"{title} succesfully downloaded ! ")


if __name__ == "__main__":
    main()
