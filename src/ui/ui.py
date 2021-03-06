from tkinter import Toplevel
from ui.sample_view import SampleView
from ui.history_view import HistoryView
from ui.login_view import LoginView
from services.sample_handler import SampleHandler
from services.user_handler import UserHandler


class UI:
    """Luokka vastaa näkymien vaihtamisesta.
    """

    def __init__(self, window):
        """Luokan konstruktori, joka luo näkymän.

        Args:
            window (window): ikkuna, johon näkymä luodaan
        """

        self.__window = window
        self.__current_view = None
        self.__sample_handler = SampleHandler()
        self.__user_handler = UserHandler()

    def start(self):
        self.__current_view = LoginView(
            self.__window, self.to_sample_view, self.__user_handler)
        self.__current_view.grid()

    def to_sample_view(self, user):
        """Metodi vaihtaa näkymää näytenäkymään.

        Args:
            user (User): käynnistyskerran sisäänkirjautunut käyttäjä
        """

        sample_view_window = Toplevel(self.__window)
        sample_view_window.title("Veriryhmäapuri")
        self.__current_view = SampleView(
            sample_view_window, self.to_history, self.__sample_handler, self.__user_handler, user)
        self.__current_view.grid()

    def to_history(self, user):
        """Metodi vaihtaa näkymää historianäkymään.

        Args:
            user (User): käynnistyskerran sisäänkirjautunut käyttäjä
        """

        history_window = Toplevel(self.__window)
        history_window.title("Näytehistoria")
        self.__current_view = HistoryView(
            history_window, self.__sample_handler, self.__user_handler, user)
        self.__current_view.grid()
