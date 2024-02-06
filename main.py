import flet
from flet import *
from flet import icons,colors
import appmenu
import section1

def main(page:page):

    page.add(
        appmenu.appmenu,
        section1.mysection,
    )

flet.app(target=main)    