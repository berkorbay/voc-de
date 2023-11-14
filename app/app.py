## Hello world example
## https://shiny.posit.co/py/docs/overview.html
import json
import random
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
import shinyswatch

# from wordlist import words
import htmltools
from htmltools import head_content, HTML, TagList, HTMLTextDocument

# global words

# with open("words.json") as f:
#     words = json.load(f)


food_words = [
    {"das Essen": "food"},
    {"die Mahlzeit": "meal"},
    {"das Frühstück": "breakfast"},
    {"das Mittagessen": "lunch"},
    {"das Abendessen": "dinner"},
    {"der Snack": "snack"},
    {"der Apfel": "apple"},
    {"die Banane": "banana"},
    {"die Orange": "orange"},
    {"die Erdbeere": "strawberry"},
    {"die Traube": "grape"},
    {"die Wassermelone": "watermelon"},
    {"das Gemüse": "vegetables"},
    {"die Karotte": "carrot"},
    {"die Tomate": "tomato"},
    {"die Kartoffel": "potato"},
    {"der Salat": "salad"},
    {"der Spinat": "spinach"},
    {"die Zwiebel": "onion"},
    {"der Knoblauch": "garlic"},
    {"das Fleisch": "meat"},
    {"das Huhn": "chicken"},
    {"der Fisch": "fish"},
    {"das Rindfleisch": "beef"},
    {"der Schweinebraten": "pork roast"},
    {"der Käse": "cheese"},
    {"die Milch": "milk"},
    {"der Joghurt": "yogurt"},
    {"die Butter": "butter"},
    {"das Brot": "bread"},
    {"die Nudeln": "pasta"},
    {"der Reis": "rice"},
    {"die Suppe": "soup"},
    {"der Kaffee": "coffee"},
    {"der Tee": "tea"},
    {"die Limonade": "lemonade"},
    {"das Wasser": "water"},
    {"der Wein": "wine"},
    {"das Bier": "beer"},
    {"der Kuchen": "cake"},
    {"der Keks": "cookie"},
    {"die Schokolade": "chocolate"},
    {"das Eis": "ice cream"},
    {"der Honig": "honey"},
    {"der Senf": "mustard"},
    {"die Mayonnaise": "mayonnaise"},
    {"das Öl": "oil"},
    {"der Essig": "vinegar"},
]


general_words = [
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

city_words = [
    [
        {"die Stadt": "city"},
        {"das Zentrum": "center"},
        {"der Bahnhof": "train station"},
        {"die U-Bahn": "subway"},
        {"die Bushaltestelle": "bus stop"},
        {"die Straße": "street"},
        {"die Kreuzung": "intersection"},
        {"der Platz": "square"},
        {"das Gebäude": "building"},
        {"der Wolkenkratzer": "skyscraper"},
        {"das Einkaufszentrum": "shopping mall"},
        {"das Kino": "cinema"},
        {"das Theater": "theater"},
        {"das Museum": "museum"},
        {"die Bibliothek": "library"},
        {"der Park": "park"},
        {"der Spielplatz": "playground"},
        {"das Café": "café"},
        {"das Restaurant": "restaurant"},
        {"die Bar": "bar"},
        {"die Diskothek": "nightclub"},
        {"der Supermarkt": "supermarket"},
        {"die Bank": "bank"},
        {"das Büro": "office"},
        {"das Rathaus": "town hall"},
        {"die Apotheke": "pharmacy"},
        {"das Krankenhaus": "hospital"},
        {"die Schule": "school"},
        {"die Universität": "university"},
        {"das Hotel": "hotel"},
        {"der Markt": "market"},
        {"der Laden": "shop/store"},
        {"das Kaufhaus": "department store"},
        {"die Post": "post office"},
        {"die Kirche": "church"},
        {"die Synagoge": "synagogue"},
        {"die Moschee": "mosque"},
        {"der Tempel": "temple"},
        {"die Brücke": "bridge"},
        {"der Fluss": "river"},
        {"der See": "lake"},
        {"der Parkplatz": "parking lot"},
        {"die Ampel": "traffic light"},
        {"der Zebrastreifen": "crosswalk"},
        {"der Fahrradweg": "bike lane"},
        {"die Treppe": "stairs"},
        {"der Aufzug": "elevator"},
        {"die Straßenbahn": "tram"},
        {"das Denkmal": "monument"},
        {"der Turm": "tower"},
    ]
]

weather_words = [
    [
        {"das Wetter": "weather"},
        {"die Sonne": "sun"},
        {"der Mond": "moon"},
        {"die Sterne": "stars"},
        {"der Himmel": "sky"},
        {"die Wolke": "cloud"},
        {"der Regen": "rain"},
        {"der Schnee": "snow"},
        {"der Hagel": "hail"},
        {"der Sturm": "storm"},
        {"der Wind": "wind"},
        {"der Nebel": "fog"},
        {"der Blitz": "lightning"},
        {"der Donner": "thunder"},
        {"die Temperatur": "temperature"},
        {"der Grad": "degree"},
        {"der Frost": "frost"},
        {"der Schauer": "shower"},
        {"der Niederschlag": "precipitation"},
        {"die Feuchtigkeit": "humidity"},
        {"der Sonnenschein": "sunshine"},
        {"die Hitze": "heat"},
        {"die Kälte": "cold"},
        {"der Frühling": "spring"},
        {"der Sommer": "summer"},
        {"der Herbst": "autumn/fall"},
        {"der Winter": "winter"},
        {"die Jahreszeit": "season"},
        {"der Sonnenaufgang": "sunrise"},
        {"der Sonnenuntergang": "sunset"},
        {"der Regenbogen": "rainbow"},
        {"der Schirm": "umbrella"},
        {"die Jacke": "jacket"},
        {"der Mantel": "coat"},
        {"die Mütze": "hat"},
        {"der Schal": "scarf"},
        {"die Handschuhe": "gloves"},
        {"die Sonnenbrille": "sunglasses"},
        {"der Strand": "beach"},
        {"die Welle": "wave"},
        {"das Gewitter": "thunderstorm"},
        {"das Klima": "climate"},
        {"die Vorhersage": "forecast"},
        {"die Wetterkarte": "weather map"},
        {"der Wetterbericht": "weather report"},
        {"der Hitzewelle": "heatwave"},
        {"die Kaltfront": "cold front"},
        {"der Tornado": "tornado"},
        {"das Erdbeben": "earthquake"},
    ]
]
global words
words = food_words + general_words + city_words + weather_words


cookie_consent = HTML(
    """

<script type="text/javascript" src="//www.freeprivacypolicy.com/public/cookie-consent/4.1.0/cookie-consent.js" charset="UTF-8"></script>
<script type="text/javascript" charset="UTF-8">
document.addEventListener('DOMContentLoaded', function () {
cookieconsent.run({"notice_banner_type":"simple","consent_type":"express","palette":"light","language":"en","page_load_consent_levels":["strictly-necessary"],"notice_banner_reject_button_hide":false,"preferences_center_close_button_hide":false,"page_refresh_confirmation_buttons":false,"website_name":"Voc-DE"});
});
</script>
<noscript>Cookie Consent by <a href="https://www.freeprivacypolicy.com/">Free Privacy Policy Generator</a></noscript>

    """
)

# Part 1: ui ----
app_ui = ui.page_bootstrap(
    head_content(cookie_consent),
    shinyswatch.theme.minty(),
    ui.row(
        ui.column(
            4,
            ui.h2("Vocabulary Builder"),
            ui.input_switch("en_de", "[🇬🇧 EN] -> [🇩🇪 DE]"),
            ui.card(
                ui.output_ui("translation_direction"),
                ui.h4(ui.output_text("new_word")),
                ui.output_text("translation"),
                ui.card_footer(
                    ui.input_action_button("show_translation", "🤞 Show"),
                    ui.input_action_button(
                        "get_new_word",
                        "🔀 New Word",
                    ),
                    style="display:flex; justify-content:space-between;",
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
    #         return "[ANSWER]"

    @reactive.Effect
    @reactive.event(input.get_new_word, ignore_none=False)
    def _():
        @output
        @render.text
        def new_word():
            if input.get_new_word:
                try:
                    the_pair = random.choice(words)
                except Exception as e:
                    print(e)
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
                return "[ANSWER]"
            else:
                return "[ANSWER]"

    @reactive.Effect
    @reactive.event(input.en_de, ignore_none=False)
    def _():
        @output
        @render.ui
        def translation_direction():
            if input.en_de._value:
                return ui.card_header("🇬🇧 EN -> 🇩🇪 DE")
            else:
                return ui.card_header("🇩🇪 DE -> 🇬🇧 EN")


# Combine into a shiny app.
# Note that the variable must be "app".
app = App(app_ui, server)
