#!/usr/bin/env python3
""" Interface of the big contest 2019 of RoboPoly. """

import sys, random
from pathlib import Path
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import int_display
import int_command


__author__ = 'Louis Munier'
__version__ = '0.1'


class Team:
    def __init__(self, team, _ski, _tchoukball, _gym):
        """Function to initialize a member of the class player."""

        # Register team name
        self.team_name = team

        # Register state of each sport
        self.state_ski = _ski
        self.state_tchoukball = _tchoukball
        self.state_gym = _gym

        # Register score of each sport
        self.score_ski = 0
        self.score_tchoukball = 0
        self.score_gym = 0
        self.score_total = 0

    def update_score(self, folder, discipline_idx, score, time):
        """Update the score for a specific player and store it."""

        if discipline_idx == ski:
            self.score_ski = score
        elif discipline_idx == tchoukball:
            self.score_tchoukball = score
        elif discipline_idx == gym:
            self.score_gym = score

        self.score_total = self.score_ski + self.score_tchoukball + self.score_gym
        self.update_file(folder, discipline_idx, score, time)

    def update_file(self, folder, discipline_idx, score, time):
        """Update the file of a specific player to have a backup."""

        # Recover all the information in the file
        with open(folder + '/{}.txt'.format(self.team_name.replace(' ', '_')), 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # now change the 2nd line, note that you have to add a newline
        data[discipline_idx] = '2 ' + str(score) + ' ' + time + '\n'
        data[-1] = str(self.score_total)

        # and write everything back
        with open(folder + '/{}.txt'.format(self.team_name.replace(' ', '_')), 'w') as file:
            file.writelines(data)


class DisplayWindow(QMainWindow, int_display.Ui_MainWindow):
    timer = QtCore.QTimer()

    def __init__(self, timer, folder, parent=None):
        """Initialize the command window and connect all the buttons to the right function."""
        super(DisplayWindow, self).__init__(parent)
        self.time_elapsed = timer       # Save timer to have elapsed time
        self.folder_storage = folder    # Save folder where all the information are stored
        self.started = False
        self.setupUi(self)

        # Init team for the first match
        with open(self.folder_storage + '/match.txt', 'r') as match_file:
            data = match_file.readlines()[match_state].split(',')

            self.name_team_ski.setText(data[ski])
            self.name_team_tchoukball.setText(data[tchoukball])
            self.name_team_gym.setText(data[gym][:-1])

        # Init timer to update elapsed time
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(10)

        # Remove frame of window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def main(self):
        """Main function to finish to implement the window."""

        self.show()

    def start_all(self):
        """Start all, the match and the timer."""

        self.started = True

    def refresh(self):
        """Refresh the total interface to have it as the initialization step."""

        # Reinitialize timer
        self.lcd_general_min.display(0)
        self.lcd_general_sec.display(0)
        self.lcd_general_millis.display(0)

        # Reinitialize times
        self.label_time_ski.setText('-:--:--')
        self.label_time_tchoukball.setText('-:--:--')
        self.label_time_gym.setText('-:--:--')

        # Reinitialize team name
        self.label_team_ski.setText('team')
        self.label_team_tchoukball.setText('team')
        self.label_team_gym.setText('team')

    def fige_time(self, discipline_idx):
        """Fige and display time for a specified discipline."""

        min = str(int(self.lcd_general_min.value()))
        sec = str(int(self.lcd_general_sec.value()))
        millis = str(int(self.lcd_general_millis.value()))

        # Display time DisplayWindow
        if discipline_idx == ski:
            self.label_time_ski.setText(min + ':' + sec + ':' + millis)
        elif discipline_idx == tchoukball:
            self.label_time_tchoukball.setText(min + ':' + sec + ':' + millis)
        elif discipline_idx == gym:
            self.label_time_gym.setText(min + ':' + sec + ':' + millis)

    def update_timer(self):
        """Update timer calling by an other timer and update with time elapsed from the beginning."""

        if self.started:
            elapsed_time = self.time_elapsed.elapsed()

            min = int(elapsed_time / 60000)
            sec = int(elapsed_time / 1000 - min * 60)
            millis = int((elapsed_time - 60000 * min - 1000 * sec) / 10)

            self.lcd_general_min.display(min)
            self.lcd_general_sec.display(sec)
            self.lcd_general_millis.display(millis)


class CommandWindow(QMainWindow, int_command.Ui_Form):
    # Set variables
    point = [[1, 2, 3, 4],
             [1, 2, 3, 3],
             [1, 2, 3, 4]]

    max_slider_value = 4

    # Set timer
    timer = QtCore.QTimer()

    def __init__(self, timer, display, teams, folder, match_state, nb_match, parent=None):
        """Initialize the command window and connect all the buttons to the right function."""

        super(CommandWindow, self).__init__(parent)
        self.display_window = display       # Save display window to interact with
        self.time_elapsed = timer           # Save timer to have elapsed time
        self.dict_teams = teams             # Save dictionary of each player class
        self.folder_storage = folder        # Save folder where all the information are stored

        self.match_state = match_state
        self.nb_match = nb_match

        self.started = False
        self.setupUi(self)

        # Init timer to update elapsed time
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(10)

        # Connect buttons to functions
        self.button_previous.clicked.connect(self.previous_match)
        self.button_next.clicked.connect(self.next_match)
        self.button_refresh.clicked.connect(self.refresh)
        self.button_start_all.clicked.connect(self.start_all)

        # Connect slider
        self.slider_ski.valueChanged.connect(
            lambda: self.update_score(ski, self.slider_ski.value(), self.display_window.name_team_ski,
                                      self.display_window.nb_points_ski, self.label_score_ski))
        self.slider_tchoukball.valueChanged.connect(
            lambda: self.update_score(tchoukball, self.slider_tchoukball.value(), self.display_window.name_team_tchoukball,
                                      self.display_window.nb_points_tchoukball, self.label_score_tchoukball))
        self.slider_gym.valueChanged.connect(
            lambda: self.update_score(gym, self.slider_gym.value(), self.display_window.name_team_gym,
                                      self.display_window.nb_points_gym, self.label_score_gym))

    def main(self):
        """Main function to finish to implement the window."""

        self.refresh()
        self.show()

    def start_all(self):
        """Start all, the match and the timer."""

        if self.started is not True:
            self.time_elapsed.restart()
            self.refresh()

        self.started = True
        self.display_window.start_all()

        # Activate sliders
        self.slider_ski.setEnabled(self.started)
        self.slider_tchoukball.setEnabled(self.started)
        self.slider_gym.setEnabled(self.started)

    def refresh(self):
        """Refresh the total interface to have it as the initialization step."""

        # Set started bool value to update vlues
        self.started = True
        self.display_window.started = True

        # Reinitialize diasplay window
        self.display_window.refresh()

        # Reinitialize sliders
        self.slider_ski.setValue(0)
        self.slider_tchoukball.setValue(0)
        self.slider_gym.setValue(0)

        # Reinitialize timer
        self.lcd_min.display(0)
        self.lcd_sec.display(0)
        self.lcd_millis.display(0)

        # Reinitialize times
        self.label_time_ski.setText('-:--:--')
        self.label_time_tchoukball.setText('-:--:--')
        self.label_time_gym.setText('-:--:--')

        self.time_elapsed.restart()

        # Reinitialize started bool value
        self.started = False
        self.display_window.started = False

        # Deactivate sliders
        self.slider_ski.setEnabled(self.started)
        self.slider_tchoukball.setEnabled(self.started)
        self.slider_gym.setEnabled(self.started)

    def previous_match(self):
        """Display the previous match."""

        self.match_state = (self.match_state - 1) % self.nb_match
        print(self.match_state)

    def next_match(self):
        """Display the next match."""

        self.match_state = (self.match_state + 1) % self.nb_match
        print(self.match_state)

    def update_score(self, discipline_idx, slider_value, disp_label_team, disp_score, command_score):
        """ Update score for a specific team."""
        time = '-:--:--'

        if self.started and disp_label_team.text() != '':
            # Compute score
            score = 0

            for val in range(slider_value):
                score += self.point[discipline_idx][val]

            # Recover time figed if slider_value = max_slider_value
            if slider_value == self.max_slider_value:
                time = self.fige_time(discipline_idx)

            # Display score CommandWindow
            command_score.setText(str(score))

            # Display score DisplayWindow
            disp_score.setText(str(score))

            # Update score in class and in file
            for t in self.dict_teams.values():
                if 'team' == disp_label_team.text():
                    t.update_score(self.folder_storage, discipline_idx, score, time)

    def fige_time(self, discipline_idx):
        """Fige and display time for a specified discipline."""
        min, sec, millis = '', '', ''

        if self.started:
            min = str(int(self.lcd_min.value()))
            sec = str(int(self.lcd_sec.value()))
            millis = str(int(self.lcd_millis.value()))

            # Display time CommandWindow
            if discipline_idx == ski:
                self.label_time_ski.setText(min + ':' + sec + ':' + millis)
            elif discipline_idx == tchoukball:
                self.label_time_tchoukball.setText(min + ':' + sec + ':' + millis)
            elif discipline_idx == gym:
                self.label_time_gym.setText(min + ':' + sec + ':' + millis)

            self.display_window.fige_time(discipline_idx)

        return min + ':' + sec + ':' + millis

    def update_timer(self):
        """Update timer calling by an other timer and update with time elapsed from the beginning."""

        if self.started:
            elapsed_time = self.time_elapsed.elapsed()

            min = int(elapsed_time / 60000)
            sec = int(elapsed_time / 1000 - min * 60)
            millis = int((elapsed_time - 60000 * min - 1000 * sec) / 10)

            self.lcd_min.display(min)
            self.lcd_sec.display(sec)
            self.lcd_millis.display(millis)


def init_team_files(folder):
    """Initialization function to init file for each team."""

    with open("team_match/team.txt", "r") as team_file:
        team = team_file.readlines()

        dictionary_teams = {}

        for t in team:
            info_team = t.split(' ')
            file = False
            name = ''

            for it in info_team:
                try:
                    int(it)

                    if not Path(folder + '/{}.txt'.format(name[:-1])).is_file() or file:
                        file = True

                        with open(folder + '/{}.txt'.format(name[:-1]), "a") as fh:
                            fh.write(str(it).replace('\n', '') + ' 0 -:--:--\n')
                except ValueError:
                    name += it + '_'

            if not Path(folder + '/{}.txt'.format(name[:-1])).is_file() or file:
                with open(folder + '/{}.txt'.format(name[:-1]), "a") as fh:
                    fh.write('0')

            dictionary_teams[name[:-1]] = Team(name[:-1].replace('_', ' '), int(info_team[-3]),
                                               int(info_team[-2]), int(info_team[-1]))

    return dictionary_teams


def init_match_file(folder, dict_teams):
    """Initialization function to init file for each match."""

    # Fill list to recover all the team participating in each sports
    list_sports = [[], [], []]

    for t in dict_teams.values():
        if t.state_ski == 1:
            list_sports[ski].append(t.team_name)
        if t.state_tchoukball == 1:
            list_sports[tchoukball].append(t.team_name)
        if t.state_gym == 1:
            list_sports[gym].append(t.team_name)

    # Find the longest list to fill the other ones with blank
    longest_list = max(list_sports, key=len)

    while len(list_sports[ski]) < len(longest_list):
        list_sports[ski].append('')

    while len(list_sports[tchoukball]) < len(longest_list):
        list_sports[tchoukball].append('')

    while len(list_sports[gym]) < len(longest_list):
        list_sports[gym].append('')

    # Fill match file
    solution = False
    list_match = []

    while not solution:
        list_match = []
        list_ski = [l for l in list_sports[ski]]
        list_tchoukball = [l for l in list_sports[tchoukball]]
        list_gym = [l for l in list_sports[gym]]

        random.shuffle(list_ski)
        random.shuffle(list_tchoukball)
        random.shuffle(list_gym)

        for m in list_ski:
            i, j = 0, 0
            match = m + ','

            while list_tchoukball[0] == m:
                i += 1

                if i == 20:
                    solution = False
                    break
                else:
                    random.shuffle(list_tchoukball)
                    solution = True

            match += list_tchoukball[0] + ','

            while list_gym[0] == m or list_gym[0] == list_tchoukball[0]:
                j += 1

                if j == 20:
                    solution = False
                    break
                else:
                    random.shuffle(list_gym)
                    solution = True

            list_match.append(match + list_gym[0] + '\n')

            list_tchoukball.pop(0)
            list_gym.pop(0)

    with open(folder + '/match.txt', "w") as match_file:
        for m in list_match:
            match_file.write(m)

    return len(longest_list)


if __name__ == "__main__":
    match_state = 0
    ski, tchoukball, gym = 0, 1, 2

    app = QApplication(sys.argv)

    # Init team and match files
    folder_name = "team_match"
    dict_teams = init_team_files(folder_name)
    nb_match = init_match_file(folder_name, dict_teams)

    # Init and start timer
    start_timer = QtCore.QElapsedTimer()
    start_timer.start()

    # Create display window
    ui_beamer = DisplayWindow(start_timer, folder_name)
    ui_beamer.main()

    # Create command window
    ui_commande = CommandWindow(start_timer, ui_beamer, dict_teams, folder_name, match_state, nb_match)
    ui_commande.main()

    sys.exit(app.exec_())