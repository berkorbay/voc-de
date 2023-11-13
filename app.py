## Hello world example
## https://shiny.posit.co/py/docs/overview.html
import json
import random
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
import shinyswatch

global words

# with open("words.json") as f:
#     words = json.load(f)

words = [
    {"der Abend": "evening"},
    {"der Wochenende": "weekend"},
    {"der Monat": "month"},
    {"das Jahr": "year"},
    {"der Geburtstag": "birthday"},
    {"die Kinder": "children"},
    {"die Eltern": "parents"},
    {"die Liebe": "love"},
    {"der Hass": "hate"},
    {"das Glück": "luck"},
    {"die Traurigkeit": "sadness"},
    {"die Freude": "joy"},
    {"der Schmerz": "pain"},
    {"die Gesundheit": "health"},
    {"die Krankheit": "illness"},
    {"der Arzt": "doctor"},
    {"das Krankenhaus": "hospital"},
    {"die Apotheke": "pharmacy"},
    {"das Telefon": "telephone"},
    {"der Computer": "computer"},
    {"das Internet": "internet"},
    {"die Musik": "music"},
    {"der Film": "movie"},
    {"das Buch": "book"},
    {"die Kunst": "art"},
    {"der Sport": "sport"},
    {"der Fußball": "football/soccer"},
    {"der Basketball": "basketball"},
    {"das Schwimmen": "swimming"},
    {"das Fahrrad": "bicycle"},
]

# Part 1: ui ----
app_ui = ui.page_bootstrap(
    shinyswatch.theme.minty(),
    ui.row(
        ui.column(
            4,
            ui.h2("Vocabulary Builder"),
            ui.input_switch("en_de", "[🇬🇧 EN] -> [🇩🇪 DE]"),
            ui.card(
                ui.card_header("🇩🇪 DE -> 🇬🇧 EN"),
                ui.output_text("new_word"),
                ui.output_text("translation"),
                ui.card_footer(
                    ui.input_action_button("show_translation", "🤞 Show"),
                    ui.input_action_button(
                        "get_new_word",
                        "🔀 New Word",
                    ),
                ),
                full_screen=False,
            ),
            offset=4,
        )
    ),
    style="margin-top:20vh;",
)


# Part 2: server ----
def server(input, output, session):
    word_pick = reactive.Value(random.choice(words))
    show_result = reactive.Value(False)

    # @output
    # @render.text
    # def translation():
    #     if input.show_translation:
    #         the_pair = word_pick.get()
    #         if input.en_de:
    #             return list(the_pair.keys())[0]
    #         else:
    #             return list(the_pair.values())[0]
    #     else:
    #         return "[SECRET]"

    @reactive.Effect
    @reactive.event(input.get_new_word, ignore_none=False)
    def _():
        @output
        @render.text
        def new_word():
            if input.get_new_word:
                the_pair = random.choice(words)
                word_pick.set(the_pair)
                show_result.set(False)
                input.show_translation._value = 0
                if input.en_de._value:
                    return list(the_pair.values())[0]
                else:
                    return list(the_pair.keys())[0]

    @reactive.Effect
    @reactive.event(input.show_translation, input.get_new_word, ignore_none=False)
    def _():
        if input.show_translation._value >= 1:
            show_result.set(True)

        @output
        @render.text
        def translation():
            if show_result.get():
                the_pair = word_pick.get()
                if input.en_de._value:
                    return list(the_pair.keys())[0]
                else:
                    return list(the_pair.values())[0]
            elif input.get_new_word:
                return "[SECRET]"
            else:
                return "[SECRET]"


# Combine into a shiny app.
# Note that the variable must be "app".
app = App(app_ui, server)
